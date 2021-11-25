## Input
Supported content types:  text/csv

##Input Details:
##Input: More than 5 comma separated csv (4 required, 2 optional)

##Details for each csv file:

- Details for each csv file:
    - scoring_date.csv (required)
        - Required columns:
            - scoring_date: scoring date for caculating signals and generate master table, format 'YYYY-MM-DD', eg: '2020-08-01'
    - creditcard_pnl.csv (required)
        - Required columns: 
            - month: month tag of the monthly report
            - age: age
            - accountID: accountID
            - credit_line: credit line at PNL date
            - tenure: tenure
            - balance_transfer_cnt: number of balance transfer records occurred in this month
            - balance_transfer_amt: amount of balance transfer records occurred in this month
            - gross_payment_cnt: number of total payment records occurred in this month
            - gross_payment_amt: amount of total payment transfer  occurred in this month
            - payment_reversal_cnt: number of payment reversal records occurred in this month
            - payment_reversal_amt: amount of payment reversal occurred in this month
            - net_payment_amt: amount of net payment occurred in this month
            - late_payment_cnt: number of late payment occurred in this month
            - auto_payment_cnt: number of auto payment occurred in this month
            - auto_pay_enrolled: whether enrolled in autopay
            - balance_amt: current balance
        - Optional column:
            - 3rd_party_credit_score: 3rd part score. Eg: FICO
    - creditcard_transaction.csv (required)
        - Required columns: 
            - trans_id: unique recordID of transaction
            - accountID: accountID associate with the transaction
            - trans_date: datetime of transaction
            - trans_amt: amount of transaction
            - is_approved: whether the transaction is approved.1 for yes, 0 for no.
            - merchantID: mechant ID 
            - MCCcode: MCC code of mechant"s industry
    - bureau_info.csv (required)
        - Required columns: 
            - month: month tag of the monthly report
            - accountID: accountID
            - NC_open_trades_ind: indicator of whether new NC trade account is opened in this month
            - NC_open_trades_cnt: number of NC trade account opened in this month
    - application_records.csv (optional)
        - Required columns: 
            - recordID: unique id of credit card application record
            - accountID: accountID associate with the record
            - application_date: date of application
            - is_approved: approved or not
    - mechant_info.csv (optional)
        - Required columns: 
            - merchantName: name of mechant
            - merchantID: mechant ID 
            - MCCcode: MCC code of mechant"s industry
            - description: description of mechant
            - risky_flag: wheter the merchant is risky

Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.
All the files mentioned above should be zipped together in a tar or tar.gz format.

Only tar and tar.gz compression formats supported.
