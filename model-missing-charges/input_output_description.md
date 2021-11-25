# Input/Output Description

> **Note**: The customer should provide the following formatted data in a JSON file. Keys should be integers. 
- _Input_: Data at the customer level (each bullet point is a field); all keys must be present, values may be
    null when specified
    - **_Line_Number_**: indicate each sample in the dataset in ascending order starting at 0 (*REQUIRED*)
        - Date type: integer (i.e. 0,1,2,3,...) 
    - **_Hospital_ID_**: corresponding hospital ID (*REQUIRED*)
        - Data type: string 
    - **_Account_ID_**: patient's account ID, unique within a hospital (*REQUIRED*)
        - Data type: string 
    - **_Patient_ID_**: patient's MRN (*REQUIRED*)
        - Data type: string 
    - **_Sex_**: patient's biological sex (Can be NULL or None)
        - Data type: string
    - **_Age_**: patient's age (Can be NULL or None)
        - Data type: integer 
    - **_Admit_Date_**: date patient came into the hospital (Can be NULL or None)
        - Data type: date in YYYY-MM-DD format (i.e. 2020-03-20)
    - **_Admit_Time_**: time patient came into the hospital (Can be NULL or None)
        - Data type: 24-hour time (i.e. 23:30)
    - **_Patient_Type_**: (Can be NULL or None)
        - Data type: string
    - **_Patient_SubType_**: (Can be NULL or None)
        - Data type: string 
    - **_Financial_Class_**: (Can be NULL or None)
        - Data type: string 
    - **_Discharge_Date_**: date patient left hospital (Can be NULL or None)
        - Data type: date in YYYY-MM-DD format (i.e. 2020-03-20)
    - **_Discharge_Time_**: time patient left hospital (Can be NULL or None)
        - Data type: 24-hour time (i.e. 23:30)
    - **_Bill_Date_**: bill drop date (Can be NULL or None)
        - Data type: date in YYYY-MM-DD format (i.e. 2020-03-20)
    - **_Transfer_Date_**: day transferred (Can be NULL or None)
        - Data type: date in YYYY-MM-DD format (i.e. 2020-03-20)
    - **_Admit_Type_**: date patient came into the hospital (Can be NULL or None)
        - Data type: string 
    - **_LOS_Days_**: length of stay in days (Can be NULL or None)
        - Data type: integer 
    - **_Charges_**: dictionary of hospital charges (*REQUIRED*)
        - keys: department code : charge code (i.e. concatenation of department code, colon and charge code)
        - values: dictionary 
            * key 1: LAST_CHG_DATE: date of last charge, in YYYY-MM-DD format
            * key 2: QUANTITY: integer value of total quantity charged
            * key 3: AMOUNT: unit price of the charge
            * key 4: REV_CODE: revenue code
            * key 5: HCPCS_CODE: HCPCS code
            * key 6: POS_COUNT: number of times code charged with positive quantity
            * key 7: NEG_COUNT: number of times code charged with negative quantity (QUANTITY - POS_COUNT)
        - Data type: dictionary
    - **_Record_Type_**: (Can be NULL or None)
        - Data type: string
    - **_Proc_Codes_**: (Can be NULL or None)
        - Data type: dictionary
            * key: procedure code (e.g. ICD10 code)
            * value: quantity
    - **_Diag_Codes_**: diagnostic code (Can be NULL or None)
        - Data type: list of strings
    - **_Prim_Diag_Code_**: primary diagnostic code (Can be NULL or None)
        - Data type: list of strings
    - **_Payer_Plan_Code_**: (Can be NULL or None)
        - Data type: list of strings
        
- _Output_: A JSON (dictionary of dictionaries) with the input's line number as the main key; for every entry there will be a prediction for that code. The JSON file can be found in the _output_data_ file. 
     - keys: line number 
     - value: dictionary 
        * keys: account ID 
        * value: dictionary 
            * keys: charge code
            * value: charge code score 

<center>

**Input Example**

</center>

```python
# THIS IS ONE WHOLE SAMPLE 
{0: {'HOSPITAL_ID': 'hosp_A',
     'ACCOUNT_ID': '0132500106',
     'PATIENT_ID': '0123456789',
     'SEX': 'F',
     'AGE': 41,
     'ADMIT_DATE': '2019-08-01',
     'ADMIT_TIME': None,
     'PATIENT_TYPE': '1',
     'PATIENT_SUBTYPE': None,
     'FINANCIAL_CLASS': '16',
     'DISCHARGE_DATE': '2019-08-04',
     'DISCHARGE_TIME': None,
     'BILL_DATE': None,
     'TRANSFER_DATE': '2019-08-05',
     'ADMIT_TYPE': None,
     'LOS_DAYS': 0,
     'CHARGES': {'101:0010187920': {'LAST_CHG_DATE': '2019-08-01',
     'QUANTITY': 0,
     'AMOUNT': 0.0,
     'REV_CODE': '340',
     'HCPCS_CODE': None,
     'POS_COUNT': 1,
     'NEG_COUNT': 1},
     '102:0051941960': {'LAST_CHG_DATE': '2019-08-01',
     'QUANTITY': 0,
     'AMOUNT': 0.0,
     'REV_CODE': '350',
     'HCPCS_CODE': 'A9110',
     'POS_COUNT': 1,
     'NEG_COUNT': 1},
     '103:0010398640': {'LAST_CHG_DATE': '2019-08-01',
     'QUANTITY': 0,
     'AMOUNT': 0.0,
     'REV_CODE': '630',
     'HCPCS_CODE': 'B1100',
     'POS_COUNT': 1,
     'NEG_COUNT': 1},
     '104:0053275920': {'LAST_CHG_DATE': '2019-08-01',
     'QUANTITY': 0,
     'AMOUNT': 0.0,
     'REV_CODE': '630',
     'HCPCS_CODE': 'B1100', 
     'POS_COUNT': 1,
     'NEG_COUNT': 1}},
     'RECORD_TYPE': None,
     'PROC_CODES': None,
     'DIAG_CODES': ['D51100'],
     'PRIM_DIAG_CODE': 'D51100',
     'PAYER_PLAN_CODE': ['OP565']}}
```

<center>

**Output Example**

</center>
<center>

```python
{
    "0": {
        "07025": 0.8,
        "G9483": 0.89,
        "Q5001": 0.84,
        "V1590": 0.86
    },
    "1": {
        "24586": 0.89,
        "A4342": 0.92
}
```
</center>
