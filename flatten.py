


'''

1) Read csv file
2) convert to flattened format
3) write to other file as output
'''
import csv as csv
import pandas as pd


'''
Returns array containing 1 at exactly one index for a race.
Array mappings are:
  [Caucasian, Asian, African American, Hispanic, and other]
  Corresponding columns in csv:
    isCaucasian
    isAsian
    isAfrican
    isAmerican
    isHispanic
    isOther
'''
def getFlattenedRace(race):
    if race == 'Caucasian':
        return [1,0,0,0,0,0]
    elif race == 'Asian':
        return [0,1,0,0,0,0]
    elif race == 'African':
        return [0,0,1,0,0,0]
    elif race == 'American':
        return [0,0,0,1,0,0]
    elif race == 'Hispanic':
        return [0,0,0,0,1,0]
    else:
        return [0,0,0,0,0,1]

'''
  [isMale, isFemale, isUnknown]
'''
def getFlattenedGender(gender):
    if gender == 'Male':
        return [1,0,0]
    elif gender == 'Female':
        return [0,1,0]
    else:
        return [0,0,1]

def getFlattenedAge(age):
    ageGroup = int(age.split('-')[0][1:])
    returnVal = [0,0,0,0,0,0,0,0,0,0]
    returnVal[ageGroup%10] = 1
    return returnVal


'''
Emergency
Urgent
Elective
Newborn
Not Available
NULL
Trauma Center
Not Mapped
'''
def getFlattenedAdmissionTypeId(admissionTypeId):
    flattened = [0]*8
    index = {'Emergency': 0,
             'Urgent': 1,
             'Elective': 2,
             'Newborn': 3,
             'Not Available': 4,
             'NULL': 5,
             'Trauma Center': 6,
             'Not Mapped': 7}[admissionTypeId]
    flattened[index] = 1
    return flattened

#TODO
def getFlattenedDischargeDispositionId(dischargeDispositionId):
    index = {'Discharged to home':0,
             'Discharged/transferred to another short term hospital':1,
             'Discharged/transferred to SNF':2,
             'Discharged/transferred to ICF':3,
             'Discharged/transferred to another type of inpatient care institution':4,
             'Discharged/transferred to home with home health service':5,
             'Left AMA':6,
             'Discharged/transferred to home under care of Home IV provider':7,
             'Admitted as an inpatient to this hospital':8,
             'Neonate discharged to another hospital for neonatal aftercare':9,
             'Expired':10,
             'Still patient or expected to return for outpatient services':11,
             'Hospice / home':12,
             'Hospice / medical facility':13,
             'Discharged/transferred within this institution to Medicare approved swing bed':14,
             'Discharged/transferred/referred another institution for outpatient services':15,
             'Discharged/transferred/referred to this institution for outpatient services':16,
             'NULL':17,
             'Expired at home. Medicaid only, hospice.':18,
             'Expired in a medical facility. Medicaid only, hospice.':19,
             'Expired, place unknown. Medicaid only, hospice.':20,
             'Discharged/transferred to another rehab fac including rehab units of a hospital .':21,
             'Discharged/transferred to a long term care hospital.':22,
             'Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.':23,
             'Not Mapped':24,
             'Unknown/Invalid':25,
             'Discharged/transferred to another Type of Health Care Institution not Defined Elsewhere':26,
             'Discharged/transferred to a federal health care facility.':27,
             'Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital':28,
             'Discharged/transferred to a Critical Access Hospital (CAH).':29}[dischargeDispositionId]
        flattened = [0]*30
        flattened[index] = 1
        return flattened


def getFlattenedAdmissionSourceId(admissionSourceId):
    index = {'PhysicianReferral':0,
             'ClinicReferral':1,
             'HMOReferral':2,
             'Transferfromahospital':3,
             'TransferfromaSkilledNursingFacility(SNF)':4,
             'Transferfromanotherhealthcarefacility':5,
             'EmergencyRoom':6,
             'Court/LawEnforcement':7,
             'NotAvailable':8,
             'Transferfromcritialaccesshospital':9,
             'NormalDelivery':10,
             'PrematureDelivery':11,
             'SickBaby':12,
             'ExtramuralBirth':13,
             'NotAvailable':14,
             'NULL':15,
             'TransferFromAnotherHomeHealthAgency':16,
             'ReadmissiontoSameHomeHealthAgency':17,
             'NotMapped':18,
             'Unknown/Invalid':19,
             'Transferfromhospitalinpt/samefacresltinasepclaim':20,
             'Borninsidethishospital':21,
             'Bornoutsidethishospital':22,
             'TransferfromAmbulatorySurgeryCenter':23,
             'TransferfromHospice':24}[admissionSourceId]
    flattened = [0] *25
    flattened[index] = 1
    return flattened


def getFlattenedDiag1(diag1):
    flattened = [0]*8

    return flattened


def getFlattenedDiag2(diag2):
    flattened = [0]*8

    return flattened


def getFlattenedDiag2(diag2):
    flattened = [0]*8

    return flattened

def getFlattenedGlucoseSerum(maxGluSerum):
    flattened = [0]*4
    if maxGluSerum == '>200':
        flattened[0] = 1
    elif maxGluSerum == '>300':
        flattened[1] = 1
    elif maxGluSerum == 'normal':
        flattened[2] = 1
    else:
        flattened[3] = 1
    return flattened




def getFlattenedDischargeDispositionIdColumnNames():
    return ['isDischarged to home','isDischarged/transferred to another short term hospital','isDischarged/transferred to SNF',
            'isDischarged/transferred to ICF','isDischarged/transferred to another type of inpatient care institution','isDischarged/transferred to home with home health service',
            'isLeft AMA','isDischarged/transferred to home under care of Home IV provider','isAdmitted as an inpatient to this hospital',
            'isNeonate discharged to another hospital for neonatal aftercare','isExpired','isStill patient or expected to return for outpatient services',
            'isHospice / home','isHospice / medical facility','isDischarged/transferred within this institution to Medicare approved swing bed',
            'isDischarged/transferred/referred another institution for outpatient services','isDischarged/transferred/referred to this institution for outpatient services',
            'isNULL','isExpired at home. Medicaid only, hospice.','isExpired in a medical facility. Medicaid only, hospice.','isExpired, place unknown. Medicaid only, hospice.',
            'isDischarged/transferred to another rehab fac including rehab units of a hospital .',
            'isDischarged/transferred to a long term care hospital.',
            'isDischarged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.',
            'isNot Mapped','isUnknown/Invalid','isDischarged/transferred to another Type of Health Care Institution not Defined Elsewhere',
            'isDischarged/transferred to a federal health care facility.',
            'isDischarged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital',
            'isDischarged/transferred to a Critical Access Hospital (CAH).']


def getFlattenedAdmissionTypeIdColumnNames():
    return ['PhysicianReferral','ClinicReferral','HMOReferral','Transferfromahospital',
            'TransferfromaSkilledNursingFacility(SNF)','Transferfromanotherhealthcarefacility','EmergencyRoom',
            'Court/LawEnforcement','NotAvailable','Transferfromcritialaccesshospital','NormalDelivery','PrematureDelivery',
            'SickBaby','ExtramuralBirth','NotAvailable','NULL','TransferFromAnotherHomeHealthAgency','ReadmissiontoSameHomeHealthAgency',
            'NotMapped','Unknown/Invalid','Transferfromhospitalinpt/samefacresltinasepclaim','Borninsidethishospital','Bornoutsidethishospital',
            'TransferfromAmbulatorySurgeryCenter','TransferfromHospice']


def getHeaders():
    header = []
    header.append('encounter_id')
    header.append('patient_nbr')
    header.extend(['isCaucasian', 'isAsian', 'isAfrican', 'isAmerican', 'isHispanic', 'isOther'])
    header.extend(['isMale', 'isFemale', 'isUnknown'])
    header.extend(['is0', 'is10', 'is20', 'is30', 'is40', 'is50', 'is60', 'is70', 'is80', 'is90'])
    header.append('weight')
    header.extend(['isEmergency','isUrgent','isElective','isNewborn','isNot Available','isNULL','isTrauma Center','isNot Mapped'])
    header.append(getFlattenedDischargeDispositionIdColumnNames())
    header.append(getFlattenedAdmissionTypeIdColumnNames())
    header.append('time_in_hospital')
    header.append('medical_specialty')
    header.append('num_lab_procedures')
    header.append('num_procedures')
    header.append('num_medications')
    header.append('number_outpatient')
    header.append('number_emergency')
    header.append('number_inpatient')
    header.append('diag_1') ##TODO : add flattened columns
    header.append('diag_2') ##TODO : add flattened columns
    header.append('diag_3') ##TODO : add flattened columns
    header.append('number_diagnoses')
    header.extend(['is>200', 'is>300', 'isNormal', 'isNone'])
    header.append('A1Cresult')
    header.append('metformin')
    header.append('repaglinide')
    header.append('nateglinide')
    header.append('chlorpropamide')
    header.append('glimepiride')
    header.append('acetohexamide')
    header.append('glipizide')
    header.append('glyburide')
    header.append('tolbutamide')
    header.append('pioglitazone')
    header.append('rosiglitazone')
    header.append('acarbose')
    header.append('miglitol')
    header.append('troglitazone')
    header.append('tolazamide')
    header.append('examide')
    header.append('citoglipton')
    header.append('insulin')
    header.append('glyburide-metformin')
    header.append('glipizide-metformin')
    header.append('glimepiride-pioglitazone')
    header.append('metformin-rosiglitazone')
    header.append('metformin-pioglitazone')
    header.append('change')
    header.append('diabetesMed')
    header.append('readmitted')


def flatten_csv(filePath):
    df = pd.read_csv(filePath, sep=',',header=0)
    flattenedRow = []
    for index, dataRow in df.iterrows():
        flattenedRow.append(dataRow['encounter_id'])
        flattenedRow.append(dataRow['patient_nbr'])
        flattenedRow.extend(getFlattenedRace(dataRow['race']))
        flattenedRow.extend(getFlattenedGender(dataRow['gender']))
        flattenedRow.extend(getFlattenedAge(dataRow['age'])
        flattenedRow.extend(getFlattenedAdmissionTypeId(dataRow['admission_type_id']))
        flattenedRow.extend(getFlattenedDischargeDispositionId(dataRow['discharge_disposition_id']))
        flattenedRow.extend(getFlattenedAdmissionSourceId(dataRow['admission_source_id']))
        flattenedRow.append(dataRow['time_in_hospital'])
        flattenedRow.append(dataRow['num_lab_procedures'])
        flattenedRow.append(dataRow['num_procedures'])
        flattenedRow.append(dataRow['num_medications'])
        flattenedRow.append(dataRow['number_outpatient'])
        flattenedRow.append(dataRow['number_emergency'])
        flattenedRow.append(dataRow['number_inpatient'])
        flattenedRow.extend(getFlattenedDiag1(dataRow['diag_1']))
        flattenedRow.extend(getFlattenedDiag1(dataRow['diag_2']))
        flattenedRow.extend(getFlattenedDiag1(dataRow['diag_3']))
        flattenedRow.append(dataRow['number_diagnoses'])
        flattenedRow.extend(getFlattenedGlucoseSerum(dataRow['max_glu_serum']))
        flattenedRow.append('0' if dataRow['A1Cresult'] == 'none' else '1')
        flattenedRow.append(dataRow['metformin'])
        flattenedRow.append(dataRow['repaglinide'])
        flattenedRow.append(dataRow['nateglinide'])
        flattenedRow.append(dataRow['chlorpropamide'])
        flattenedRow.append(dataRow['glimepiride'])
        flattenedRow.append(dataRow['acetohexamide'])
        flattenedRow.append(dataRow['glipizide'])
        flattenedRow.append(dataRow['glyburide'])
        flattenedRow.append(dataRow['tolbutamide'])
        flattenedRow.append(dataRow['pioglitazone'])
        flattenedRow.append(dataRow['rosiglitazone'])
        flattenedRow.append(dataRow['acarbose'])
        flattenedRow.append(dataRow['miglitol'])
        flattenedRow.append(dataRow['troglitazone'])
        flattenedRow.append(dataRow['tolazamide'])
        flattenedRow.append(dataRow['examide'])
        flattenedRow.append(dataRow['citoglipton'])
        flattenedRow.append(dataRow['insulin'])
        flattenedRow.append(dataRow['glyburide-metformin'])
        flattenedRow.append(dataRow['glipizide-metformin'])
        flattenedRow.append(dataRow['glimepiride-pioglitazone'])
        flattenedRow.append(dataRow['metformin-rosiglitazone'])
        flattenedRow.append(dataRow['metformin-pioglitazone'])

        flattenedRow.append(dataRow['change'])
        flattenedRow.append(dataRow['diabetesMed'])
        flattenedRow.append(dataRow['readmitted'])

        break

flatten_csv('./diabetic_data.csv')
