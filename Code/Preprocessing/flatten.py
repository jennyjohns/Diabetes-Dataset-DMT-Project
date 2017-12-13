


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
    flattened = [0]*9
    flattened[int(admissionTypeId)] = 1
    return flattened

#TODO
def getFlattenedDischargeDispositionId(dischargeDispositionId):
    flattened = [0]*30
    flattened[int(dischargeDispositionId)] = 1
    return flattened


def getFlattenedAdmissionSourceId(admissionSourceId):
    flattened = [0] *26
    flattened[int(admissionSourceId)] = 1
    return flattened


'''
Circulatory
Respiratory
Digestive
Diabetes
Injury
Musculoskeletal
Genitourinary
Neoplasms
Other
'''
def getFlattenedDiag1(diag1):
    if diag1.isdigit() == False:
        index = 8
    else:
        diag = int(float(diag1))

        if ((diag >= 390 and diag <= 459) or diag == 785):
            index = 0
        elif ((diag >= 460 and diag <= 519) or diag == 786):
            index = 1
        elif ((diag >= 520 and diag <= 579) or diag == 787):
            index = 2
        elif (diag == 250):
            index = 3
        elif (diag >= 800 and diag <= 999):
            index = 4
        elif (diag >= 710 and diag <= 739):
            index = 5
        elif ((diag >= 580 and diag <= 629) or diag == 788):
            index = 6
        elif ((diag >= 140 and diag <= 239) or (diag >= 790 and diag <= 799) or (diag >= 680 and diag <= 709) or
              (diag >= 1 and diag <= 139) or diag in [782, 780, 781, 784]):
            index = 7
        else:
            index = 8

    flattened = [0]*9
    flattened[index] = 1

    return flattened


def getFlattenedDiag2(diag2):
    return getFlattenedDiag1(diag2)


def getFlattenedDiag2(diag3):
    return getFlattenedDiag1(diag3)

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

'''

'''
def getFlattenedReadmitted(readmitted):
    if readmitted == '<30':
        index = 0
    elif readmitted == '>30':
        index = 1
    else:
        index = 2

    flattened = [0]*3
    flattened[index] = 1
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


def getFlattenedAdmissionSourceTypeIdColumnNames():
    return ['PhysicianReferral','ClinicReferral','HMOReferral','Transferfromahospital',
            'TransferfromaSkilledNursingFacility(SNF)','Transferfromanotherhealthcarefacility','EmergencyRoom',
            'Court/LawEnforcement','NotAvailable','Transferfromcritialaccesshospital','NormalDelivery','PrematureDelivery',
            'SickBaby','ExtramuralBirth','NotAvailable','NULL','TransferFromAnotherHomeHealthAgency','ReadmissiontoSameHomeHealthAgency',
            'NotMapped','Unknown/Invalid','Transferfromhospitalinpt/samefacresltinasepclaim','Borninsidethishospital','Bornoutsidethishospital',
            'TransferfromAmbulatorySurgeryCenter','TransferfromHospice']


def getFlattenedDiag1Columns():
    return ['isDiag1Circulatory','isDiag1Respiratory','isDiag1Digestive','isDiag1Diabetes',
            'isDiag1Injury','isDiag1Musculoskeletal','isDiag1Genitourinary','isDiag1Neoplasms',
            'isDiag1Other']

def getFlattenedDiag2Columns():
    return ['isDiag2Circulatory','isDiag2Respiratory','isDiag2Digestive','isDiag2Diabetes',
            'isDiag2Injury','isDiag2Musculoskeletal','isDiag2Genitourinary','isDiag2Neoplasms',
            'isDiag2Other']

def getFlattenedDiag3Columns():
    return ['isDiag2Circulatory','isDiag2Respiratory','isDiag2Digestive','isDiag2Diabetes',
            'isDiag2Injury','isDiag2Musculoskeletal','isDiag2Genitourinary','isDiag2Neoplasms',
            'isDiag2Other']


def getHeaders():
    header = []
    header.append('encounter_id')
    header.append('patient_nbr')
    header.extend(['isCaucasian', 'isAsian', 'isAfrican', 'isAmerican', 'isHispanic', 'isOther'])
    header.extend(['isMale', 'isFemale', 'isUnknown'])
    header.extend(['is0', 'is10', 'is20', 'is30', 'is40', 'is50', 'is60', 'is70', 'is80', 'is90'])
    header.extend(['isEmergency','isUrgent','isElective','isNewborn','isNot Available','isNULL','isTrauma Center','isNot Mapped', 'None'])
    header.extend(getFlattenedDischargeDispositionIdColumnNames())
    header.extend(getFlattenedAdmissionSourceTypeIdColumnNames())
    header.append('time_in_hospital')
    header.append('medical_specialty')
    header.append('num_lab_procedures')
    header.append('num_procedures')
    header.append('num_medications')
    header.append('number_outpatient')
    header.append('number_emergency')
    header.append('number_inpatient')
    header.extend(getFlattenedDiag1Columns())
    header.extend(getFlattenedDiag2Columns())
    header.extend(getFlattenedDiag3Columns())
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
    header.extend(['is<30', 'is>30', 'isNo'])
    return header

def writeToFile(allFlattenedRows):
    df = pd.DataFrame(allFlattenedRows)
    df.to_csv('flattened.csv', mode='a', index=False, header=False)

def flatten_csv(filePath):
    df = pd.read_csv(filePath, sep=',',header=0)
    allFlattenedRows = []
    allFlattenedRows.append(getHeaders())

    for index, dataRow in df.iterrows():
        flattenedRow = []
        flattenedRow.append(dataRow['encounter_id'])
        flattenedRow.append(dataRow['patient_nbr'])
        flattenedRow.extend(getFlattenedRace(dataRow['race']))
        flattenedRow.extend(getFlattenedGender(dataRow['gender']))
        flattenedRow.extend(getFlattenedAge(dataRow['age']))
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
        flattenedRow.append('0' if dataRow['A1Cresult'] == 'None' else '1')
        flattenedRow.append('0' if dataRow['metformin'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['repaglinide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['nateglinide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['chlorpropamide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['glimepiride'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['acetohexamide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['glipizide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['glyburide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['tolbutamide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['pioglitazone'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['rosiglitazone'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['acarbose'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['miglitol'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['troglitazone'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['tolazamide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['examide'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['citoglipton'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['insulin'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['glyburide-metformin'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['glipizide-metformin'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['glimepiride-pioglitazone'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['metformin-rosiglitazone'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['metformin-pioglitazone'] == 'No' else '1')

        flattenedRow.append('0' if dataRow['change'] == 'No' else '1')
        flattenedRow.append('0' if dataRow['diabetesMed'] == 'No' else '1')
        flattenedRow.extend(getFlattenedReadmitted(dataRow['readmitted']))

        allFlattenedRows.append(flattenedRow)

        if(len(allFlattenedRows) == 10000):
            writeToFile(allFlattenedRows)
            allFlattenedRows = []
    writeToFile(allFlattenedRows)
        

flatten_csv('../Dataset/diabetic_data.csv')

