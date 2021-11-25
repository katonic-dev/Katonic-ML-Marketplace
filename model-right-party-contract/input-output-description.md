## Input Files

> **Note**: The customer should provide the following formatted data in CSV files. The files should then be archived and zipped into a single file e.g. input.tar.gz 

- Input: 5 comma separated csv (5 required)
- Details for each csv file:
    - scoring_date.csv (required)
        - Required columns:
            - scoring_date: scoring date for caculating signals and generate main table, format 'YYYY-MM-DD', eg: '2020-01-01'
    - account_profile.csv (required)
        - Required columns: 
            - acct_key: Unique Identifier of an account
            - snapshot_date: the record snapshot date
            - dlqncy_cycle_nbr: Delinquency Cycle Number, only accounts with Cycle 1 & 2 are required for scoring
            - coll_proc_code: Collection Process Code. All accounts in collection are assigned to any one 
            - pay_protcd_ind: Payment Protection Indicator
            - payment_code: Payment Status Code
            - acct_open_date: Account Open Date 
            - cycle_date: account cycle date
            - perf_mth: month tag of snapshot_date 
    - creditcard_pnl.csv (required)
        - Required columns: 
            - acct_key: Unique Identifier of an account
            - perf_mth: Month tag
            - cycle_open_to_buy_amt: Available credit at cycle time.
    - creditcard_bureau.csv (required)
        - Required columns: 
            - acct_key: Unique Identifier of an account
            - perf_mth: Month tag 
            - FICO_score: FICO score
            - off_us_utilization: Off-Us Utilization
    - call_activity.csv (required)
        - Required columns: 
            - acct_key: Unique Identifier of an account
            - call_date: Call Date 
            - call_start_time: Call Start Time
            - call_end_time: Call End Time
            - mobile_ind: indicator if the account is a mobile phone
            - RPC_ind: indicator if the account holder picks up the phone
            - phone_type: Phone Type (Home ,Work,Other)
    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.

## Output
- A json response containing 'account_key'  with original order, and one more column added named 'Score' which contains model's prediction of RPC likelihood scores of account.


