## Input
Supported content types:  text/csv

## Input Details:
## Input: More than 5 comma separated csv (depending on how many service usage the user will provide)

## Details for each csv file:
- scoring_date.csv (required)
    - Required columns:
        - scoring_date: scoring date for caculating signals and generate master table, format 'YYYY-MM-DD', eg: '2020-08-01'
- profile.csv (required)
    - Required columns: 
        - email_address: Email Address ID
        - tenure
        - LATITUDE (optional)
        - LONGITUDE (optional)
        - age
        - customer_income
- email_sent.csv (required)
    - Required columns: 
        - email_address: Email Address ID
        - email_sent_time: Timestamp email sent to customer
        - email_sent_record_id: record ID associated with the email
- email_click.csv (required)
    - Required columns: 
        - email_address: Email Address ID
        - email_click_time: Timestamp email clicked by customer
        - email_click_record_id: record ID associated with the email
- email_open.csv (required)
    - Required columns: 
        - email_address: Email Address ID
        - email_open_time: Timestamp email opened by customer
        - email_open_record_id: record ID associated with the email
- transactions.csv (required)
    - Required columns: 
        - email_address: Email Address ID
        - transaction_date: Timestamp of the transaction
        - transaction_amount: Dollar Amount of Transaction (should be numerical, no dollar signs)
        - coupons_used: Number of coupons used
        - product_id: Integer corresponding to Product, starting from 1 (ex 1, 2, 3, 4...)
        - transaction_id: id of the transaction
- dm_sent.csv (optional)
    - Required columns:
        - email_address: Email Address ID
        - dm_sent_date:  Timestamp direct mail was sent
        - dm_sent_record_id: Direct Mail ID
    
Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.
All the files mentioned above should be zipped together in a tar.gz format.

Only tar and tar.gz compression formats supported.
