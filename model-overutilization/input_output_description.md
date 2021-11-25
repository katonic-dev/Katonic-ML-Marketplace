# Input/Output Description

### Input 
The input dataset is in json format. Each key in the outermost dictionary represents an account. All keys must be present unless specified as optional. Values may be null when specified.

* keys: integer (i.e. 1,2,3,...) indicate each account in the dataset, in ascending order, starting at 1 (REQUIRED)
* values: dictionary(containing information about the account)  
    * Key: **ACCOUNT_ID**
    * Value: Corresponding account ID (REQUIRED) 
        * Data type: String 
    * Key: **PATIENT_ID**
    * Value: Corresponding patient ID (REQUIRED) 
        * Data type: String 
    * Key: **ADMIT_DATE**
    * Value: Visit date for outpatient and emergency visits. Admission date for inpatient visits (REQUIRED) 
        * Data type: String with YYYY-MM-DD format (REQUIRED) 
    * Key: **DISCHARGE_DATE**
    * Value: Visit date for outpatient and emergency visits. Discharge date for inpatient visits (REQUIRED) 
        * Data type: String with YYYY-MM-DD format(REQUIRED)  
    * Key: **PATIENT_TYPE**
    * Value: Patient type(I: Inpatient, O: Outpatient, E: Emergency, etc) (REQUIRED) 
        * Data type: String (REQUIRED) 
    * Key: **PATIENT_SUB_TYPE**
    * Value: Patient sub-type (OPTIONAL) 
        * Data type: String (REQUIRED) 
    * Key: **SEX**
    * Value: Patient sex (REQUIRED) 
        * Data type: String (REQUIRED) 
    * Key: **AGE**
    * Value: Patient age (REQUIRED) 
        * Data type: String (REQUIRED) 
    * Key: **LOS_DAYS**
    * Value: Visit length of stay in days (OPTIONAL) 
        * Data type: float (REQUIRED)  
    * Key: **PROV_NPI**
    * Value: Provider's NPI (REQUIRED) 
        * Data type: String (REQUIRED) 
    * Key: **PROV_SPEC**
    * Value: Provider's specialty (OPTIONAL) 
        * Data type: String (REQUIRED) 
    * Key: **PROV_TYPE**
    * Value: Provider's type (e.g. M.D., Anesthetist, etc) (OPTIONAL) 
        * Data type: String (REQUIRED)                                                                    
    * Key: **CHARGES**
    * Value: dictionary of visit charges billed (REQUIRED) 
        * Keys: department code:charge code (i.e. concatenation of department code, colon and charge code)
        * Values: dictionary
            * Key: LAST_CHG_DATE
            * Value: date of last charge
                * Data type: String with YYYY-MM-DD format 
            * Key: QUANTITY 
            * Value: Number of units charged 
                * Data type: Integer                                        
            * Key: AMOUNT 
            * Value: Unit price of the charge 
                * Data type: Float (dollar amount)    
            * Key: REV_CODE 
            * Value: Revenue code 
                * Data type: String    
            * Key: HCPCS_CODE 
            * Value: Equivalent HCPCS code 
                * Data type: String     
    * Key: **PROC_CODES**
    * Value: Procedure codes billed (OPTIONAL)
        * Data type: list of strings (Can be empty) 
    * Key: **PROC_CODE_TYPE**
    * Value: Dictionary containing type of procedure codes (HCPCS, CPT, etc.) (REQUIRED if PROC_CODES is not empty)
        * Keys: procedure codes 
        * Values: Procedure code types
            * Data type: string
    * Key: **PRIM_DIAG_CODE**
    * Value: Visit's primary diagnosis code (REQUIRED)
        * Data type: String (REQUIRED)
    * Key: **SEC_DIAG_CODE**
    * Value: Visit's secondary diagnosis code (OPTIONAL)
        * Data type: String
    * Key: **DIAG_CODE_TYPE**
    * Value: Version of ICD codes used (ICD9 or ICD10) (REQUIRED)
        * Data type: String (REQUIRED)                 
    * Key: **PAYER_PLAN_CODE**
    * Value: Payer's plan code (OPTIONAL)
        * Data type: String (REQUIRED) 

### Output
A JSON file (dictionary of dictionaries) called code_lvl_scores.json in ./output directory, which contains each account from the input directory. The output contains the patient ID, visit provider's NPI, charge codes and their associated over-utilization risk score; codes with higher scores have a higher risk of having been over-utilized.

* Keys: Integer (i.e. 1,2,3,...) indicate each sample in the dataset in ascending order starting at 1 (REQUIRED)
* Values: Dictionary of patient IDs, NPIs and the charge codes' risk score
    * Key: PATIENT_ID
    * Value: Corresponding patient ID
    * Key: PROVIDER_NPI
    * Value: Visit provider's NPI
    * Keys: Charge codes
    * Values: Risk scores associated with each charge code

 -Reference file: input_data.json.out
