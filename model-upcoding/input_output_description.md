# Input/Output Description

## Input:
A **json file** with claim details in the below format. Reference file: sample.json

- key: integer (i.e. 1,2,3,...) indicate each sample in the dataset in ascending order starting at 1 (REQUIRED)
- value: dictionary
  - key: __ACCOUNT_ID__
  - value: corresponding account ID (REQUIRED)
    - data type: string
  - key: __PATIENT_ID__
  - value: corresponding patient ID (REQUIRED)
    - data type: string
  - key: __ADMIT_DATE__
    - value: visit date for outpatient and emergency visits. Admission date for inpatient visits (REQUIRED) 
      - data type: string with YYYY-MM-DD format
  - key: __DISCHARGE_DATE__
    - value: visit date for outpatient and emergency visits. Discharge date for inpatient visits (REQUIRED) 
      - data type: string with YYYY-MM-DD format
  - key: __PATIENT_TYPE__
  - value: corresponding patient type: I: Inpatient, O: Outpatient, E: Emergency, etc. (REQUIRED)
    - data type: string
  - key: __PATIENT_SUBTYPE__
  - value: corresponding patient subtype (OPTIONAL)
    - data type: string (Can be NULL or None)
  - key: __SEX__
  - value: corresponding patient biological sex (M/F) (OPTIONAL)
    - data type: string (Can be NULL or None)
  - key: __AGE__
  - value: corresponding patient AGE (OPTIONAL)
    - data type: integer (Can be NULL or None)
  - key: __LOS_DAYS__
  - value: length of stay in days (OPTIONAL)
    - data type: integer (Can be NULL or None)
  - key: __PROV_NPI__
  - value: provider's NPI or ID (REQUIRED)
    - data type: string 
  - key: __PROV_SPEC__
  - value: provider's specialty (OPTIONAL)
    - data type: string (Can be NULL or None)
  - key: __PROV_TYPE__
  - value: provider's type such as M.D., Anesthetist, RN, etc. (OPTIONAL)
    - data type: string (Can be NULL or None)
  - key: __CHARGES__
  - value: dictionary of hospital charges (REQUIRED)
    - keys: __department code__:__charge code__ (i.e. concatenation of department code, colon and charge code)
    - value: dictionary
      - key: __LAST_CHG_DATE__
      - value: date of last charge
        - data type: string with YYYY-MM-DD format
      - key: __QUANTITY__
      - value: integer value of total quantity charged
        - data type: integer
      - key: __AMOUNT__
      - value: unit price of the charge
        - data type: dollar amount (i.e. 23.50)
      - key: __REV_CODE__
      - value: revenue code
        - data type: string
      - key: __HCPCS_CODE__
      - value: HCPCS code
        - data type: string
  - key: __PROC_CODES__
  - value: procedure code (OPTIONAL)
    - data type: list of strings (Can be empty)
  - key: __PROC_CODE_TYPE__
  - value: dictionary (OPTIONAL)
    - keys: procedure codes
    - values: procedure code type (i.e. CPT, HCPCS, etc.)
      - data type: string
  - key: __PRIM_DIAG_CODE__
  - value: primary diagnostic code (REQUIRED)
    - data type: list of strings
  - key: __SEC_DIAG_CODE__
  - value: secondary diagnostic code (OPTIONAL)
    - data type: list of strings (Can be empty)
  - key: __DIAG_CODE_TYPE__
  - value: dictionary (REQUIRED)
    - keys: diagnostic codes
    - values: diagnostic code type (i.e. ICD10, ICD9, etc.)
      - data type: string
  - key: __PAYER_PLAN_CODE__
  - value: plan code (OPTIONAL)
    - data type: string (Can be NULL or None)


## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.json.out

|     Column     |                                         Meaning                                               | 
|----------------|-----------------------------------------------------------------------------------------------|      
| PROV_NPI       | Provider ID                                                                                   |
| RISK_SCORE     | Risk scores - providers use more high-value codes compared to the average for their specialty |------------------------------------------------------------------------------------------------------------------
