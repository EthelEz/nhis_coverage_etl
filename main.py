from dotenv import load_dotenv, find_dotenv
import os
import json
from fhirpy import AsyncFHIRClient, SyncFHIRClient
from processing import HmoCode, convert_csv2_json, transform_date, transform_gender, date_id, HmoCategory
from processing import get_principal_id, get_spouse_id, get_fchild_id, get_schild_id, get_tchild_id, get_ftchild_id, coverage_id

_ = load_dotenv(find_dotenv())
api_url = os.environ['local_url']

csv_nhia = os.environ['csv_nhia']
json_nhia = os.environ['json_nhia']

nhis_coverage_data = convert_csv2_json(csv_nhia, json_nhia)


async def main():
    client = SyncFHIRClient(
        url=api_url,
        extra_headers={"Content-Type":"application/json"}
    )

    with open(os.path.join(json_nhia), 'r') as file:
        coverages = json.load(file)
    
    for data in coverages:
        organization = client.resource(
            'Organization',
            id=data.get("hospital_no").lower().strip(),
            identifier=[{"system":"http://term.hl7.org/CodeSystem/hospital", "value": data.get("hospital_no")}],
            active=False,
            type=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/organization", "code": data.get("hospital_no"), "display": "NHIA Nigeria Healthcare Provider"}]}],
            name=data.get("Hospital_name"),
            address=[{"line": [data.get("Hospital_name")]}]
        )
        organization.save()

        if organization['active'] is False:
            organization.active = True
        organization.save()
        print(organization.id)

        patient = client.resource(
            "Patient",
            id=get_principal_id(data),
            active=False,
            name=[{"family": data.get("Principal First Name"), "given":[data.get("Principal Surname")]}],
            birthDate=transform_date(data.get("Principal DoB")),
            gender=transform_gender(data.get("Principal gender")),
            identifier=[{"use": "official", "system": "http://fhir.nhs.uk/Id/nhis", "value": data.get("NHIS ID")}],
            managingOrganization={"type": "Organization", "reference": "Organization"+'/'+organization['id']}
        )
        patient.save()

        if patient['active'] is False:
            patient.active = True 
        patient.save()

        related_spouse = client.resource(
            "RelatedPerson",
            id=get_spouse_id(data),
            active=False,
            patient={"reference": "Patient"+'/'+patient["id"]},
            relationship=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/spouse", "code": "S", "display": "Spouse"}]}],
            name=[{"use": "official", "family": data.get("Spouse First Name"), "given": [data.get("Spouse SurName")]}],
            gender=transform_gender(data.get("Spouse Gender")),
            birthDate=transform_date(data.get("Spouse DoB")),
            identifier=[{"use": "official", "system": "http://fhir.nhs.uk/Id/nhis", "value": data.get("NHIS ID")}]
        )

        if data.get("Spouse First Name") and data.get("Spouse SurName"):

            related_spouse.save()

            if related_spouse['active'] is False:
                related_spouse.active = True 
            related_spouse.save()
        
        related_child_1 = client.resource(
            "RelatedPerson",
            id=get_fchild_id(data),
            active=False,
            patient={"reference": "Patient"+'/'+patient["id"]},
            relationship=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/child_1", "code": "C1", "display": "Child 1"}]}],
            name=[{"use": "official", "family": data.get("Child 1 First Name"), "given": [data.get("Child 1 Surname")]}],
            gender=transform_gender(data.get("Child 1 Gender")),
            birthDate=transform_date(data.get("Child 1 DoB")),
            identifier=[{"use": "official", "system": "http://fhir.nhs.uk/Id/nhis", "value": data.get("NHIS ID")}],

        )

        if data.get("Child 1 First Name") and data.get("Child 1 Surname"):

            related_child_1.save()

            if related_child_1['active'] is False:
                related_child_1.active = True 
            related_child_1.save()
        
        related_child_2 = client.resource(
            "RelatedPerson",
            id=get_schild_id(data),
            active=False,
            patient={"reference": "Patient"+'/'+patient["id"]},
            relationship=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/child_2", "code": "C2", "display": "Child 2"}]}],
            name=[{"use": "official", "family": data.get("Child 2 First Name"), "given": [data.get("Child 2 Surname")]}],
            gender=transform_gender(data.get("Child 2 Gender")),
            birthDate=transform_date(data.get("Child 2 DoB")),
            identifier=[{"use": "official", "system": "http://fhir.nhs.uk/Id/nhis", "value": data.get("NHIS ID")}],

        )

        if data.get("Child 2 First Name") and data.get("Child 2 Surname"):

            related_child_2.save()

            if related_child_2['active'] is False:
                related_child_2.active = True 
            related_child_2.save()
        
        related_child_3 = client.resource(
            "RelatedPerson",
            id=get_tchild_id(data),
            active=False,
            patient={"reference": "Patient"+'/'+patient["id"]},
            relationship=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/child_3", "code": "C3", "display": "Child 3"}]}],
            name=[{"use": "official", "family": data.get("Child 3 First Name"), "given": [data.get("Child 3 Surname")]}],
            gender=transform_gender(data.get("Child 3 Gender")),
            birthDate=transform_date(data.get("Child 3 DoB")),
            identifier=[{"use": "official", "system": "http://fhir.nhs.uk/Id/nhis", "value": data.get("NHIS ID")}],

        )
        if data.get("Child 3 First Name") and data.get("Child 3 Surname"):

            related_child_3.save()

            if related_child_3['active'] is False:
                related_child_3.active = True 
            related_child_3.save()

        related_child_4 = client.resource(
            "RelatedPerson",
            id=get_ftchild_id(data),
            active=False,
            patient={"reference": "Patient"+'/'+patient["id"]},
            relationship=[{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/child_4", "code": "C4", "display": "Child 4"}]}],
            name=[{"use": "official", "family": data.get("Child 4 First Name"), "given": [data.get("Child 4 Surname")]}],
            gender=transform_gender(data.get("Child 4 Gender")),
            birthDate=transform_date(data.get("Child 4 DoB")),
            identifier=[{"use": "official", "system": "http://fhir.nhs.uk/Id/nhis", "value": data.get("NHIS ID")}],

        )
        if data.get("Child 4 First Name") and data.get("Child 4 Surname"):

            related_child_4.save()

            if related_child_4['active'] is False:
                related_child_4.active = True 
            related_child_4.save()

        nhis_coverage = client.resource(
            "Coverage",
            id=coverage_id(data),
            identifier=[{"system": "http://nhis.org/certificate", "value":data.get("NHIS ID")}],
            status="draft",
            type={"coding": [{"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode","code": "ENO164P","display": "extended healthcare"}]},
            # policyHolder={"reference": "http://nhis.org/FHIR/Organization"+'/'+hmo_data(data)},
            subscriber={"reference": "Patient"+'/'+patient['id']},
            beneficiary={"reference": "Patient"+'/'+patient['id']},
            dependent=data.get("dependant")
        )
        nhis_coverage["class"] = []
        if data.get("HMO"):
            nhis_coverage["class"].append({"value": HmoCode(data.get("HMO")).codes(), "name": data.get("HMO")})

        nhis_coverage.payor = []

        if data.get("Spouse First Name"):
            nhis_coverage.payor.append({"reference": "RelatedPerson"+'/'+related_spouse.id, "display": "Spouse"})
        if data.get("Child 1 First Name"):
            nhis_coverage.payor.append({"reference": "RelatedPerson"+'/'+related_child_1.id, "display": "Child 1"})
        if data.get("Child 2 First Name"):
            nhis_coverage.payor.append({"reference": "RelatedPerson"+'/'+related_child_2.id, "display": "Child 2"})
        if data.get("Child 3 First Name"):
            nhis_coverage.payor.append({"reference": "RelatedPerson"+'/'+related_child_3.id, "display": "Child 3"})
        if data.get("Child 4 First Name"):
            nhis_coverage.payor.append({"reference": "RelatedPerson"+'/'+related_child_4.id, "display": "Child 4"})

        nhis_coverage.save()

        if nhis_coverage['status'] == "draft":
            nhis_coverage.status = "active"
        nhis_coverage.save()

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())