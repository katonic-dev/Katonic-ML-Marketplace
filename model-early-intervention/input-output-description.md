## Input Files

> **Note**: The customer should provide the following formatted data in CSV files. The files should then be archived and zipped into a single file e.g. input.tar.gz 

- Input: 4 comma separated csv (4 required)
- Details for each csv file:
    - PNL.csv (required)
        - Required columns: 
            - acc_id: Account ID
            - month_tag: Year Month
            - tenure: account tenure
            - portf_id: Portfolio ID
            - fico_score: fico score
            - bucket_cd: bucket code
            - totl_credt_limit: total credit limit
            - balance_amt: balance amount
            - spend_amt: sepnd amount
            - payment_amt: payment amount
            - balcon_amt: balcon amount
            - ca_amt: cash advance amount
            - late_fee: late payment fee
            - gcl: gross credit loss
            - recovery: gross credit loss * recovery rate
            - interest: interest 
    - Bureau.csv (required)
        - Required columns: 
            - acc_id: Account ID
            - month_tag: Year Month
            - inq_6m_ct: the number of inquiries in the last 6 months.
            - major_delnq_ct: the number of major delinquencies.
            - rbont_rvlv_cl_amt: Revolving credit limit of bank; oil; and national cards
            - hi_debt_burdn_pct: highest percent debt burden for revolving/bank/national trade lines
            - totl_rvlv_bal_amt: Total Revolving Balance of Open Bank/Finance/Natl/Retail/Oil Trades
            - totl_bal_amt: the dollar balance at the time of the balance control activity.
            - totl_bnkcrd_cl_amt: aggregate revolving bankcard credit limit.
            - totl_mortg_bal_amt: Total balance of mortgage
            - opn_rvlv_bnkcrd_cnt: Number of Open BankCard Revolving Tradelines (used in ranking arrtibutes)
            - delinquency_bankcard_month_age: the time since most recent delinquency for Bankcard trades
            - hi_delnq_bankcard_12m: highest delinquency on any bank revolving trade line in the last 12 months.
        - Optional columns: 
            - totl_tl_ct: the total number of trade lines
    - Transaction.csv (required)
        - Required columns: 
            - trans_id: Unique record ID of transaction
            - acc_id: Account ID associate with the transaction
            - trans_date: Datetime of transaction
            - trans_amt: Amount of transaction
            - is_approved: Whether the transaction is approved
            - zip_code: zip code
        - Optional columns: 
            - customer_id: Customer ID
            - MCC_code: MCC code of mechant's industry
    - Authorization.csv (required)
        - Required columns: 
            - auth_id: Authorization ID
            - acc_id: Account ID associate with the authorization
            - auth_date: Authorization Date
            - auth_amt: Authorization amount
            - auth_code: Authorization code
            - auth_decline_reason_code: Authorization decline reason code
            - auth_type_code: Authorization type code
            - zip_code: zip code
    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.

## Output
- A json response containing 'acc_id'  with original order, and one more column added named 'Score' which contains model's prediction of early intervention likelihood scores of account.

