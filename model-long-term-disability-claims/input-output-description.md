## Input Files

> **Note**: The customer should provide the following formatted data in 6 CSV files. The files should then be archived and zipped into a single file e.g. input.tar.gz 

- _Input_: Data at the customer level (each bullet point is a field); all IDs must be present. Below are the details for each CSV file. 

    - **_Employees.csv_** (*REQUIRED*): 

    | Column            | Required | Meaning                                                                
    |-------------------|----------|--------------------------------------------------------------|
    | member_id         | Y        | Member ID                                                    |
    | plan_id           | Y        | Plan ID                                                      |         
    | cov_cd            | Y        | Coverage code (type)                                         |         
    | age               | Y        | Age of member                                                |         
    | sic_cd            | Y        | Standard industry code                                       |         
    | memb_country      | Y        | Member's country                                             |         
    | memb_state        | Y        | Member's state                                               |         
    | memb_zip          | Y        | Zip code of the member                                       |         
    | memb_sal          | Y        | Member annual salary                                         |         
    | employment_tenure | Y        | Member's tenure in years with their employment               |         
    | gender            | N        | Member's gender                                              |         
    | family_status     | N        | Family status: single, spouse, spouse and children, children | 
    -----------------------------------------------------------------------------------------------

    - **_Billing.csv_** (*REQUIRED*): 

    | Column            | Required | Meaning                             
    |-------------------|----------|----------------------------------------------|
    | plan_id           | Y        | Plan ID                                      |
    | member_id         | Y        | Member ID                                    |
    | bill_num_id       | Y        | Bill number ID                               |
    | bill_type_id      | Y        | Specific billing type ID (e.g. Life, LT, ST) |
    | bill_create_dt    | N        | Bill create date                             |
    | bill_due_dt       | N        | Bill due date                                |
    | memb_bill_prem_am | N        | Member premium amount                        |
    | memb_bill_vol_am  | N        | Member voluntary amount                      |
    -------------------------------------------------------------------------------

    - **_Claims.csv_** (*REQUIRED*):

    | Column         | Required | Meaning                      |
    |----------------|----------|------------------------------|
    | plan_id        | Y        | Plan ID                      |
    | member_id      | Y        | Member ID                    |
    | clm_record_id  | Y        | Claim record ID              |
    | clm_rec_dt     | Y        | Claim received date          |
    | cov_cd         | Y        | Coverage code (type)         |
    | tot_chrg_am    | N        | Total charge amount          |
    | inelig_chrg_am | N        | Ineligible charge amount     |
    | ded_am         | N        | Deductible amount            |
    | coins_am       | N        | Coinsurance amount           |
    | pymt_am        | N        | Payment amount               |
    | pymt_dt        | N        | Payment date                 |
    | is_approved    | N        | Is claim approved for member |
    ------------------------------------------------------------

    - **_Plan.csv_** (*REQUIRED*):
    
    | Column       | Required | Meaning                           |
    |--------------|----------|-----------------------------------|
    | plan_id      | Y        | Plan ID                           |
    | plan_size    | Y        | Member count                      |
    | plan_tenure  | Y        | Plan tenure in years              |
    | plan_eff_dt  | Y        | Plan effective date               |
    | plan_term_dt | Y        | Plan termination date             |
    | sic_cd       | Y        | Primary Standard Industry Code    |
    | mail_zip5_cd | Y        | Employer zip code                 |
    | elig_emp_ct  | N        | Total count of eligible employees |
    | renewal_dt   | N        | Plan renewal date                 |
    ---------------------------------------------------------------

    - **_Coverage.csv_** (*REQUIRED*): 

    | Column        | Required | Meaning                                                                   |
    |---------------|----------|---------------------------------------------------------------------------|
    | plan_id       | Y        | Plan ID                                                                   |
    | cov_cd        | Y        | Coverage code                                                             |
    | cov_eff_dt    | N        | Coverage effective date                                                   |
    | cov_term_dt   | N        | Coverage termination date                                                 |
    | vol_am        | N        | Voluntary amount                                                          |
    | prem_am       | N        | Premium amount                                                            |
    | emp_contrb_in | N        | Employee contribution indicator (e.g. Y/N)                                |
    | dep_contrb_in | N        | Dependent contribution indicator (e.g. Y/N)                               |
    | elim_days     | N        | Coverage elimination days (time from disability to time receive payments) |
    --------------------------------------------------------------------------------------------------------

    - **_Dependent.csv_**: 

    | Column       | Required | Meaning               |
    |------------- |----------|-----------------------|
    | member_id    | Y        | Member ID             |
    | dependent_id | Y        | Dependent ID          |
    | member_rela  | N        | Member relationship   |
    | age          | N        | Age of dependent      |
    | gender       | N        | Gender of dependent   |
    ---------------------------------------------------

## Output
- _Output_: A Json response with each employee's ID as the main key; for every entry, there will be **two** predictions in **two** different columns. Both predictions will be given for the employee ID in each row. The *_ltd_clm_prob_* column will contain the probability of an incident occurring. The *_ltd_clm_tot_amt_* column will contain the expected amount the insurance will pay for the long-term disability. 

    | Column          | Required | Meaning                      |
    |-----------------|----------|------------------------------|
    | member_id       | Y        | Member ID                    |
    | ltd_clm_prob    | N        | Probability of LTD incident  |
    | ltd_clm_tot_amt | N        | Expected LTD claims amount   |
    -------------------------------------------------------------