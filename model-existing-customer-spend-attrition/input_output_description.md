# Input/Output Description
- _Input_: Data at the customer level (each bullet point is a field); all IDs must be present. Below are the details for each CSV file. 

    - **_Bureau.csv_** (*REQUIRED*): 

    | Column              | Required | Meaning                                                                    |
    |---------------------|----------|----------------------------------------------------------------------------|
    | acc_id              | Y        | Account's unique ID                                                        |
    | portf_id            | Y        | Unique portfolio ID for a specific account                                 |
    | bur_id              | Y        | Unique credit bureau ID                                                    |
    | month_tag           | Y        | Month tag of the monthly report                                            |
    | bont_mro_mon_ct     | Y        | Number of days since most recent open bank trade opened                    |
    | off_us_rvlv_cl_amt  | Y        | The total credit limit in dollars of all off-us bank revolving trade lines |
    | off_us_brt_bal_amt  | Y        | The total balance owed on all off-us bank revolving trade lines            |
    | hi_debt_burdn       | N        | Highest percent debt burden for revolving/bank/national trade lines        |
    | risk_score          | Y        | Customer's risk score                                                      |
    | age_tl              | N        | Age of oldest trade lines                                                  |
    | avg_opn_bnkcrd      | N        | Average age of open bank cards                                             |
    | bankr_ind           | N        | Indicate if any bankruptcies                                               |
    | totl_opn_tl_cnt     | N        | Total number of opened trade lines                                         |
    | opn_rvlv_bnkcrd_cnt | N        | Number of open bank card revolving tradelines                              |
    | rbont_rvlv_cl_amt   | N        | Revolving credit limit of bank; oil; and national cards                    |
    | low_cl_limit        | N        | Lowest credit limit on open bank card                                      |
    | opn_tl_months       | N        | Months since most recently opened trade line                               |
    | hi_bnkcrd_util      | N        | Highest utilization of revolving trade lines                               |
    | bnkcrd_util_cnt     | N        | Total number of revolving trade lines with utilization                     |
    | totl_bnkcrd_util    | N        | Total balance utilization (percent)                                        |
    | totl_delnq_cnt      | N        | Total delinquency count                                                    |
    ---------------------------------------------------------------------------------------------------------------

    - **_PNL.csv_** (*REQUIRED*): 

    | Column      | Required | Meaning                                |
    |-------------|----------|----------------------------------------|
    | acc_id      | Y        | Account's unique ID                    |
    | month_tag   | Y        | Month tag of the monthly report        |
    | credt_limit | Y        | Credit limit                           |
    | credt_bal   | Y        | Credit card balance for the month      |
    | purch_amt   | Y        | Purchasing amount                      |
    | payment     | Y        | Payment amount                         |
    | interest    | Y        | Interest                               |
    | closing_bal | Y        | Closing amount at end of billing cycle |
    -------------------------------------------------------------------
    
    - **_Transaction.csv_** (*REQUIRED*): 

    | Column        | Required | Meaning                                             |
    |---------------|----------|-----------------------------------------------------|
    | acc_id        | Y        | Account's unique ID                                 |
    | trans_type_id | Y        | Transaction type ID associate with the transactions |
    | month_tag     | Y        | Month tag of the monthly report                     |
    | trans_amt     | Y        | Transaction amount for the month                    |
    | trans_cnt     | Y        | Number of transactions for the month                |
    | is_approved   | Y        | Whether the transactions are approved               |
    | merch_id      | N        | Unique merchant ID associated with MCC code         |
    | mcc_code      | N        | MCC code of merchant's industry                     |
    | mcc_descrip   | N        | MCC code description                                |
    ----------------------------------------------------------------------------------
	
- Output: a JSON list of objects contaning, for each record in the original order the following fields:
    - acc_id: Account's unique ID
	- pred_delta_spend:  Prediction of how much spending (in dollars) will increase or decrease in the next 12 months
 - Reference file: sample.zip.out