from hmo_search import search
import csv
import json


class HmoCode:
    def __init__(self, hmo):
        self.hmo = hmo
    def codes(self):
        if self.hmo == "Hygeia HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "Total Health Trust Limite":
            return search(self.hmo, "name", "code")
        if self.hmo == "Clearline International Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "HCI Healthcare Limited (formerly Healthcare International Nig. Ltd).":
            return search(self.hmo, "name", "code")
        if self.hmo == "Mediplan Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Aiico-Multishield HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "United Healthcare International Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Ronsberger HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "International  Health Management Services Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Songhai HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "Integrated Health Care Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Sunu Healthcare Services Limited (formerly Managed Healthcare Services Limited)":
            return search(self.hmo, "name", "code")
        if self.hmo == "Princeton Health Ltd":
            return search(self.hmo, "name", "code")
        if self.hmo == "Venus Medicare Ltd":
            return search(self.hmo, "name", "code")
        if self.hmo == "Defence Health Maintenance Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "United Comprehensive Healthcare":
            return search(self.hmo, "name", "code")
        if self.hmo == "Veritas Healthcare Limited (formerly Health Care Security Limited)":
            return search(self.hmo, "name", "code")
        if self.hmo == "Royal Health Maintenance Services Ltd":
            return search(self.hmo, "name", "code")
        if self.hmo == "Zuma Health":
            return search(self.hmo, "name", "code")
        if self.hmo == "Markfema Nigeria Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Prepaid Medicare Services Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Sterling Health Managed Care Services Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Health Partners Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Precious Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Oceanic Health Management Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Wellness Health Management Services Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "GreenBay Healthcare Services Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Medexia  Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Marina Medical Services (HMO) Ltd":
            return search(self.hmo, "name", "code")
        if self.hmo == "Non-Such Medicare Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Salus Trust GTE Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Prohealth HMO Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Axa-Mansard Health Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "GNI Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Ultimate  Health Management Services":
            return search(self.hmo, "name", "code")
        if self.hmo == "Avon Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Regenix Healthcare Service Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Redcare Health Services Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Well Health Network Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Ives Medicare":
            return search(self.hmo, "name", "code")
        if self.hmo == "Medicare Alliance Limited (formerly Doma Healthcare Limited)":
            return search(self.hmo, "name", "code")
        if self.hmo == "Police Health Maintenance Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Novo Health Africa Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Anchor HMO International Company Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Metrohealth HMO Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Greenfield Health Management Ltd":
            return search(self.hmo, "name", "code")
        if self.hmo == "LifeWorth Medicare Ltd":
            return search(self.hmo, "name", "code")
        if self.hmo == "NNPC HMO Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Health Assur Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Phillips Health Management Services":
            return search(self.hmo, "name", "code")
        if self.hmo == "Ashmed Integrated Health Services":
            return search(self.hmo, "name", "code")
        if self.hmo == "Leadway Health Limited (formerly Ankara Services Limited)":
            return search(self.hmo, "name", "code")
        if self.hmo == "Synergy Wellcare Medicaid Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Reliance HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "Roding Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Fountain Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Hallmark HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "Bastion Health Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Maayoit Healthcare Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Century Medicaid Services Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Rothauge Healthcare Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Royal Exchange Healthcare Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "A&M Healthcare Trust Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Masslife Healthcare Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Skyda Health Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Peramare Health Management Co. Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Springtide Healthcare Services Ltd. (HMO)":
            return search(self.hmo, "name", "code")
        if self.hmo == "Seraph Nigeria Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Grooming Health Management Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "Kennedia HMO":
            return search(self.hmo, "name", "code")
        if self.hmo == "MB & O Healthcare Services Ltd.":
            return search(self.hmo, "name", "code")
        if self.hmo == "Alleanza Health Management Limited":
            return search(self.hmo, "name", "code")
        if self.hmo == "GORAH Healthcare Limited":
            return search(self.hmo, "name", "code")


class HmoCategory:
    def __init__(self, hmo):
        self.hmo = hmo
    def category(self):
        if self.hmo == "Hygeia HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "Total Health Trust Limite":
            return search(self.hmo, "name", "category")
        if self.hmo == "Clearline International Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "HCI Healthcare Limited (formerly Healthcare International Nig. Ltd).":
            return search(self.hmo, "name", "category")
        if self.hmo == "Mediplan Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Aiico-Multishield HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "United Healthcare International Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Ronsberger HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "International  Health Management Services Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Songhai HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "Integrated Health Care Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Sunu Healthcare Services Limited (formerly Managed Healthcare Services Limited)":
            return search(self.hmo, "name", "category")
        if self.hmo == "Princeton Health Ltd":
            return search(self.hmo, "name", "category")
        if self.hmo == "Venus Medicare Ltd":
            return search(self.hmo, "name", "category")
        if self.hmo == "Defence Health Maintenance Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "United Comprehensive Healthcare":
            return search(self.hmo, "name", "category")
        if self.hmo == "Veritas Healthcare Limited (formerly Health Care Security Limited)":
            return search(self.hmo, "name", "category")
        if self.hmo == "Royal Health Maintenance Services Ltd":
            return search(self.hmo, "name", "category")
        if self.hmo == "Zuma Health":
            return search(self.hmo, "name", "category")
        if self.hmo == "Markfema Nigeria Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Prepaid Medicare Services Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Sterling Health Managed Care Services Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Health Partners Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Precious Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Oceanic Health Management Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Wellness Health Management Services Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "GreenBay Healthcare Services Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Medexia  Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Marina Medical Services (HMO) Ltd":
            return search(self.hmo, "name", "category")
        if self.hmo == "Non-Such Medicare Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Salus Trust GTE Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Prohealth HMO Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Axa-Mansard Health Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "GNI Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Ultimate  Health Management Services":
            return search(self.hmo, "name", "category")
        if self.hmo == "Avon Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Regenix Healthcare Service Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Redcare Health Services Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Well Health Network Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Ives Medicare":
            return search(self.hmo, "name", "category")
        if self.hmo == "Medicare Alliance Limited (formerly Doma Healthcare Limited)":
            return search(self.hmo, "name", "category")
        if self.hmo == "Police Health Maintenance Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Novo Health Africa Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Anchor HMO International Company Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Metrohealth HMO Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Greenfield Health Management Ltd":
            return search(self.hmo, "name", "category")
        if self.hmo == "LifeWorth Medicare Ltd":
            return search(self.hmo, "name", "category")
        if self.hmo == "NNPC HMO Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Health Assur Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Phillips Health Management Services":
            return search(self.hmo, "name", "category")
        if self.hmo == "Ashmed Integrated Health Services":
            return search(self.hmo, "name", "category")
        if self.hmo == "Leadway Health Limited (formerly Ankara Services Limited)":
            return search(self.hmo, "name", "category")
        if self.hmo == "Synergy Wellcare Medicaid Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Reliance HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "Roding Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Fountain Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Hallmark HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "Bastion Health Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Maayoit Healthcare Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Century Medicaid Services Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Rothauge Healthcare Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Royal Exchange Healthcare Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "A&M Healthcare Trust Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Masslife Healthcare Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Skyda Health Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Peramare Health Management Co. Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Springtide Healthcare Services Ltd. (HMO)":
            return search(self.hmo, "name", "category")
        if self.hmo == "Seraph Nigeria Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Grooming Health Management Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "Kennedia HMO":
            return search(self.hmo, "name", "category")
        if self.hmo == "MB & O Healthcare Services Ltd.":
            return search(self.hmo, "name", "category")
        if self.hmo == "Alleanza Health Management Limited":
            return search(self.hmo, "name", "category")
        if self.hmo == "GORAH Healthcare Limited":
            return search(self.hmo, "name", "category")
        
def convert_csv2_json(csvFilePath, jsonFilePath):    
    data = []
    with open(csvFilePath, encoding='ISO-8859-1') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(rows)
    with open(jsonFilePath, 'w', encoding='ISO-8859-1') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

def transform_date(date_str):
    from datetime import datetime
    if date_str:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date

def date_id(date_str):
    from datetime import datetime

    if date_str:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        formatted_id = date_obj.strftime("%Y%m%d")
        return formatted_id

def transform_gender(gender):
    if gender == "M":
        return "male"
    elif gender == "F":
        return "female"
    else:
        return "Unknown"

def get_principal_id(data: dict):
    nhis = data.get("NHIS ID")
    principal_fname = data.get("Principal First Name")
    principal_dob = data.get("Principal DoB")

    if nhis and principal_fname and principal_dob:
        return str(f"{nhis}-{principal_fname}-{date_id(principal_dob)}".lower().strip())
    else:
       return "no-principal-data"

def get_spouse_id(data: dict):
    nhis = data.get("NHIS ID")
    spouse_fname = data.get("Spouse First Name")
    spouse_dob = data.get("Spouse DoB")

    if nhis and spouse_fname and spouse_dob:
        return str(f"{nhis}-{spouse_fname}-{date_id(spouse_dob)}".lower().strip())
    else:
       return "no-spouse_data"

def get_fchild_id(data: dict):
    nhis = data.get("NHIS ID")
    fchild_fname = data.get("Child 1 First Name")
    fchild_dob = data.get("Child 1 DoB")

    if nhis and fchild_fname and fchild_dob:
        return str(f"{nhis}-{fchild_fname}-{date_id(fchild_dob)}".lower().strip())
    else:
       return "no-fchild-data"
    
def get_schild_id(data: dict):
    nhis = data.get("NHIS ID")
    schild_fname = data.get("Child 2 First Name")
    schild_dob = data.get("Child 2 DoB")

    if nhis and schild_fname and schild_dob:
        return str(f"{nhis}-{schild_fname}-{date_id(schild_dob)}".lower().strip())
    else:
       return "no-schild-data"

def get_tchild_id(data: dict):
    nhis = data.get("NHIS ID")
    tchild_fname = data.get("Child 3 First Name")
    tchild_dob = data.get("Child 3 DoB")

    if nhis and tchild_fname and tchild_dob:
        return str(f"{nhis}-{tchild_fname}-{date_id(tchild_dob)}".lower().strip())
    else:
       return "no-tchild-data"
    
def get_ftchild_id(data: dict):
    nhis = data.get("NHIS ID")
    ftchild_fname = data.get("Child 4 First Name")
    ftchild_dob = data.get("Child 4 DoB")

    if nhis and ftchild_fname and ftchild_dob:
        return str(f"{nhis}-{ftchild_fname}-{date_id(ftchild_dob)}".lower().strip())
    else:
       return "no-ftchild-data"

# data.get("NHIS ID")+'-'+data.get("NIN").replace("/", "").lower().strip())
def get_ftchild_id(data: dict):
    nhis = data.get("NHIS ID")
    ftchild_fname = data.get("Child 4 First Name")
    ftchild_dob = data.get("Child 4 DoB")

    if nhis and ftchild_fname and ftchild_dob:
        return str(f"{nhis}-{ftchild_fname}-{date_id(ftchild_dob)}".lower().strip())
    else:
       return "no-ftchild-data"
    
def coverage_id(coverage: dict):
    nhis = coverage.get("NHIS ID")
    nin = coverage.get("NIN")

    if nhis and nin:
        return str(f"{nhis}-{nin}".replace("/", "").lower().strip())
    else:
        return "no-coverage-data"
    
# def hmo_data(hmo: dict):
#     hmo = hmo.get("HMO")

#     if hmo:
#         return HmoCode(hmo).codes()
#     else:
#         return "no-hmo-data"