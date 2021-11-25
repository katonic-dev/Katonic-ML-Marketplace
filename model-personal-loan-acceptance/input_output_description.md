# Input/Output Description
- Input: A **zip file** with the following comma separated csv files. Reference file: sample.zip

- Data at the customer level (each bullet point is a field); all IDs must be present. Below are the details for each CSV file. 

    - **_Agent.csv_** (*REQUIRED*): 

    | Column         | Required | Meaning                                                      |
    |----------------|----------|--------------------------------------------------------------|
    | agent_id       | Y        | Agent ID                                                     |
    | apps_closed    | Y        | Amount of applications agent closed for the month            |
    | total_num_apps | Y        | Agent's total monthly application amount                     |
    | drop_off_rate  | Y        | Ratio of agent's clients canceled/withdrew application       |
    | month_tag      | Y        | Month tag of the monthly report                              |
    | avg_month_apr  | N        | Average APR for applications used by the agent for the month |
    | accpt_rate     | Y        | Percent of customers that accepted the application           |
    --------------------------------------------------------------------------------------------

    - **_Bureau.csv_** (*REQUIRED*): 

    | Column        | Required | Meaning                                                                                      |
    |---------------|----------|----------------------------------------------------------------------------------------------|
    | bureau_id     | Y        | Bureau's unique ID                                                                           |
    | acc_id        | Y        | Account's unique ID                                                                          |
    | month_tag     | Y        | Month tag of the monthly report                                                              |
    | auto_amt      | Y        | Indicates whether there is an initial loan amount(HC/CL) of open auto loan in the last month |
    | debt_burdn    | Y        | debt burden                                                                                  |
    | fico_score    | Y        | Customer's fico score                                                                        |
    | age_tl_ct     | Y        | Age of oldest trade lines                                                                    |
    | bankr_ind     | Y        | Indicate if any bankruptcies                                                                 |
    | totl_opn_tl   | Y        | Total number of opened trade lines                                                           |
    | opn_tl_months | Y        | Months since most recently opened trade line                                                 |
    | totl_tl_ct    | Y        | Total number of trade lines                                                                  |
    | mort_amt      | Y        | Highest initial loan amount (HC/CL) of open mortgage                                         |
    | mort_pay      | Y        | Average of current monthly payment amount of mort_amt                                        |
    ---------------------------------------------------------------------------------------------------------------------------

    - **_Application.csv_** (*REQUIRED*): 
    > **Note**: Column __seg_tag__ can take a None value.

    | Column       | Required | Meaning                                                                                                 |
    |--------------|----------|---------------------------------------------------------------------------------------------------------|
    | app_id       | Y        | Application's unique ID                                                                                 |
    | acc_id       | Y        | Account's unique ID                                                                                     |
    | month_tag    | Y        | Month tag of the monthly report                                                                         |
    | loan_Id      | Y        | Loan ID                                                                                                 |
    | loan_apr     | Y        | Loan APR                                                                                                |
    | loan_type    | Y        | Loan type (i.e. Credit Card, Loan, ID Theft Protection, etc)                                            |
    | loan_amt     | Y        | Loan amount                                                                                             |
    | canceled     | Y        | Indicate whether customer canceled the loan application (i.e. 1 = True, 0 = False)                      |
    | withdrawn    | Y        | Indicate whether customer withdrew from the loan application (i.e. 1 = True, 0 = False)                 |
    | loan_ind     | Y        | Indicate whether customer was approved or declined for the loan (i.e. 1 = Approved, 0 = Declined)       |
    | credit_line  | Y        | Indicate whether customer was granted a Credit line (i.e. 1 = Approved, 0 = Declined)                   |
    | own_or_rent  | Y        | Indicate whether customer is a homeowner or rents (i.e. Renter, Owner)                                  | 
    | comments     | Y        | Comments made by customers who cancel/withdrew (None if customer didn't cancel/withdraw loan)           |
    | chann_source | Y        | Channel used to reach customer (i.e. Mail, Internet, Phone, Internet and Phone)                         |
    | date         | Y        | Date which agent reached out                                                                            |
    | prop_type    | Y        | Property type code                                                                                      |
    | hobbies      | N        | Hobbies/Interests                                                                                       |
    | veh_ind      | Y        | Indicates whether the customer owns an vehicle (i.e. 1 = True, 0 = False, None = no info)               |
    | veh_age      | N        | Main vehicles age in years                                                                              |
    | assets       | Y        | Assets (i.e. Boat, RV, etc.)                                                                            |
    | seg_tag      | N        | Customer Segmentation Tags if available (i.e. stable family, average joe, etc. and None if unavailable) |
    -------------------------------------------------------------------------------------------------------------------------------------

    - **_Account.csv_** (*REQUIRED*):

    | Column        | Required | Meaning                                                            |
    |---------------|----------|--------------------------------------------------------------------|
    | acc_id        | Y        | Account's unique ID                                                |
    | app_id        | Y        | Application's unique ID                                            |
    | month_tag     | Y        | Month tag of the monthly report                                    |
    | open_date     | Y        | Date account opened                                                |
    | card_act_date | Y        | Date activated credit card                                         |
    | acc_type      | Y        | Account type (i.e. Joint/Individual/Business)                      |
    | acc_status    | Y        | Account status (i.e. Open/Closed/Normal/Delinquent/Overlimit/etc.) |
    | acc_ind       | Y        | Indicate if the account is main or supplementary                   |
    -------------------------------------------------------------------------------------------------

     - **_PNL.csv_** (*REQUIRED*):
     > **Note**: Column __credt_fee__  and __delinq_lvl__ can take a None value.

    | Column           | Required | Meaning                                                                                                   |
    |------------------|----------|-----------------------------------------------------------------------------------------------------------|
    | acc_id           | Y        | Account's unique ID                                                                                       |
    | month_tag        | Y        | Month tag of the monthly report                                                                           |
    | totl_credt_limit | Y        | Total credit limit                                                                                        |
    | credt_interest   | Y        | Interest                                                                                                  |
    | ca_amt           | Y        | Total dollar amount of cash advances for the current billing cycle                                        |
    | credt_bal        | Y        | Credit card balance for the month                                                                         |
    | min_pay          | Y        | Min Payment Amount                                                                                        |
    | credt_fee        | Y        | Type of credit card fee (i.e. Balance Transfer, Cash Advance, Expedited Payment, etc. and None if no fee) |
    | delinq_lvl       | Y        | Delinquency level (i.e. 30 days, 60 days, etc. and None if no delinquency level)                          |
    -------------------------------------------------------------------------------------------------------------------------------------------
 
    - **_Transaction.csv_** (*OPTIONAL*): 

    | Column      | Required | Meaning                                   |
    |-------------|----------|-------------------------------------------|
    | trans_id    | Y        | Unique record ID of transaction           |
    | acc_id      | Y        | Account ID associate with the transaction |
    | trans_date  | Y        | Datetime of transaction                   |
    | trans_amt   | Y        | Amount of transaction                     |
    | is_approved | Y        | Whether the transaction is approved       |
    | MCC_code    | N        | MCC code of the merchant's industry       |
    ----------------------------------------------------------------------    
- Output: A list of JSON objects with the Account ID as the main key. For every Account ID, **_there will be 2_** additional columns. The **_chann_source_** column contains the source in which an agent reached out to a customer. The **_seg_tag_** is 1 of the 9 segment groups the Personal Loan Acceptance Model predicts for each customer. Reference file: sample.zip.out

    | Column       | Meaning                                                                             |
    |--------------|-------------------------------------------------------------------------------------|
    | acc_id       | Account's unique ID                                                                 |
    | chann_source | Channel used to reach the customer (i.e. Mail, Internet, Phone, Internet and Phone) | 
    | seg_tag      | Customer Segmentation Tags                                                          |
    ------------------------------------------------------------------------------------------------------
  -  Segments (9): 
    * **_Secure Family_**
        - High disposable income
        - High request
        - Stable housing
    * **_Secure, Stable Occupation_**
        - Long term home owners
        - Traditional/Small but stable occupation
    * **_Retired, Good Credit_**
        - Good credit
        - Retired/office/professional
        - Medium debt-income
        - Low request
    * **_Average, Stable Occupation_**
        - Medium fico
        - Low debt-income
        - Stable job
        - New home owners
    * **_Bad Credit Professionals_**
        - Bad credit
        - High mover 
        - Educators/professional with average disposable income
    * **_Debt, Small Occupation_**
        - Health/other small occupation
        - High debt-income home owners
    * **_Retired, Bad Credit_**
        - Bad credit
        - Retired
        - Low disposable income
        - Low request
    * **_New Home-Owners, Unstable Occupation_**
        - High request
        - New home-owners
        - Low-disposable income
    * **_Young Renters, Unstable Occupation_**
        - Young
        - Low disposable income
        - Renters
        - Service industry
