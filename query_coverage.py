from dotenv import load_dotenv, find_dotenv
import os
from fhirpy import SyncFHIRClient
# import asyncio

# Load environment variables
_ = load_dotenv(find_dotenv())
api_url = os.environ['local_url']
identifier = os.environ['identifier']

def fetch_related_person(client, person_id):
    """Fetch related person details by ID."""
    related_person_data = client.resources('RelatedPerson').search(_id=person_id).fetch_all()
    return related_person_data

def fetch_patient(client, patient_id):
    """Fetch patient details by ID."""
    patient_data = client.resources('Patient').search(_id=patient_id).fetch_all()
    return patient_data

def extract_person_details(person_details, role, index=None):
    """Extract details from a related person or patient resource."""
    firstname = person_details.get_by_path("name.0.given.0")
    lastname = person_details.get_by_path("name.0.family")
    dob = person_details.get("birthDate")
    gender = person_details.get("gender")
    identifier_id = person_details.get_by_path("identifier.0.value")
    if role == "Spouse":
        return {
            "Spouse ID": identifier_id,
            "Spouse Firstname": firstname,
            "Spouse Lastname": lastname,
            "Spouse DoB": dob,
            "Spouse Gender": gender
        }
    elif role == "Principal":
        return {
            "Principal ID": identifier_id,
            "Principal Firstname": firstname,
            "Principal Lastname": lastname,
            "Principal DoB": dob,
            "Principal Gender": gender
        }
    else:
        return {
            f"Child{index} ID": identifier_id,
            f"Child{index} Firstname": firstname,
            f"Child{index} Lastname": lastname,
            f"Child{index} DoB": dob,
            f"Child{index} Gender": gender
        }

def extract_coverage_data(client, coverage):
    """Extract coverage and related persons data."""
    coverage_data = []

    # Fetch class and principal information
    class_name = coverage.get_by_path("class.0.name")
    class_code = coverage.get_by_path("class.0.value")
    principal_reference = coverage.get_by_path("subscriber.reference")
    dependent = coverage.get("dependent")

    # Base coverage information
    coverage_info = {
        "Hospital Name": class_name,
        "Hospital Code": class_code,
        "Dependent": dependent
    }

    # print("Extracting coverage data for:", coverage_info)

    # Fetch principal details
    if principal_reference:
        principal_id = principal_reference.split('/')[1]
        principal_data = fetch_patient(client, principal_id)
        for principal_details in principal_data:
            person_details = extract_person_details(principal_details, "Principal")
            # Merge base coverage info with person details
            combined_data = {**coverage_info, **person_details}
            coverage_data.append(combined_data)

    # Fetch payor details
    payors = coverage.get("payor")
    if payors:
        for i in range(len(payors)):
            payor_display = coverage.get_by_path(f"payor.{i}.display")
            payor_reference = coverage.get_by_path(f"payor.{i}.reference")
            if payor_reference is not None:
                payor_id = payor_reference.split('/')[1]
                if payor_display == "Spouse":
                    spouse_data = fetch_related_person(client, payor_id)
                    for spouse_details in spouse_data:
                        person_details = extract_person_details(spouse_details, "Spouse")
                        # Merge base coverage info with person details
                        combined_data = {**coverage_info, **person_details}
                        coverage_data.append(combined_data)
                elif payor_display.startswith("Child"):
                    child_data = fetch_related_person(client, payor_id)
                    for child_details in child_data:
                        person_details = extract_person_details(child_details, "Child", i)
                        # Merge base coverage info with person details
                        combined_data = {**coverage_info, **person_details}
                        coverage_data.append(combined_data)

    return coverage_data

async def main():
    api_url = os.environ['local_url']
    identifier = os.environ['identifier']
    client = SyncFHIRClient(url=api_url, extra_headers={"Content-Type": "application/json"})

    response = client.resources("Coverage").search(identifier=f"{identifier}").fetch_all()
    all_coverage_data = []

    for coverage in response:
        coverage_data = extract_coverage_data(client, coverage)
        if coverage_data:
            all_coverage_data.extend(coverage_data)

    print("All coverage data:", all_coverage_data)

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
