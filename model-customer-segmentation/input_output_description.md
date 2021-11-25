# Input/Output Description

- Input: A zip file containing 5 comma separated csv files. Reference file: sample.zip
- Details for each csv file:
    - scoring_date.csv (required)
        - Required columns:
            - scoring_date: scoring date for caculating signals and generate master table, format 'YYYY-MM-DD', eg: '2020-08-01'
    - accounts.csv (required) : This is a table analagous to a log for each customer. It contains information about things like flights or hotels booked, checking in or checking out of a hotel or flight, adding a phone line, sending an SMS or receiving an email, etc.
        - Required columns: 
            - activity_id: unique ID associated with this table
            - account_id: id associated with the account
            - customer_id: id associated with the customer on the account
            - activity_date: timestamp associated with the account activity
            - service_id: service id associated with the account activity
    - profiles.csv (required) : This is a table containing customer information. It is pretty generic and contains one row for each customer. There can be multiple customers per account_id.
        - Required columns: 
            - profile_id: unique id associated with this table
            - account_id: id associated with the account
            - customer_id: id associated with the customer on the account
            - balance: balance associated with customer_id
            - age
            - customer_income
            - latitude (optional)
            - longitude (optional)
    - services.csv (required) : This is a generalized table for different kinds of services. Start date can refer to when someone checks into a hotel room, end date when they check out. This can also apply to flights booked, when they boarded, and when the flight lands. It can also refer to when someone starts and ends a subscription to a cable or phone service.
        - Required columns: 
            - unique_id: unique id associated with this table
            - account_id: id associated with the account
            - customer_id: record ID associated with the customer
            - service_id: service id associated with the service record
            - service_start_date: service start timestamp or date
            - service_end_date: service end timestamp or date
    - transactions.csv (required) : This is a table similar to accounts, but limited to transaction types of activity involving a dollar amount.
        - Required columns: 
            - transaction_id: unique id associated with this table
            - account_id: id associated with the account
            - customer_id: id associated with the customer on the account
            - transaction_date: Timestamp of the transaction
            - transaction_amount: Dollar Amount of Transaction (should be numerical, no dollar signs)
            - service_id: service id associated with the transaction
- Output: JSON list of objects with field 'cluster' which contains model's prediction of the cluster/segment for the record. Reference file: sample.zip.out
