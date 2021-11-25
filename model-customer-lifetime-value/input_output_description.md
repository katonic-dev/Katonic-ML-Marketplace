# Input/Output Description
- Input: A **zip file** with the following comma separated csv files. Reference file: sample.zip
- Details of each csv file:
    - account_profile.csv (required)
        - Required columns: 
            - acc_id: account identifier 
            - perf_month: year month
            - acc_needstate: account needstate/segmentation
            - acc_type: account type, like Business, Government, Individual,…
            - tenure: account tenure

    - service1_usage.csv (required)
        - Required columns: 
            - record_id: uniqe id of each service1 usage record
            - acc_id: account identifier 
            - record_time: date of the service usage record of the account
            - amount: amount of service1 usage


    - serviceN_usage.csv (optional, N=2,3,4,5...**)
        - Required columns: 
            - record_id: uniqe id of each servicec2 usage record
            - acc_id: account identifier 
            - record_time: date of the service usage record of the account
            - amount: amount of service2 usage
            - **N=2,3,4,5,6,7...., can add any number of service usage table, follow the same schema of service1_usage_records.csv

    - payment.csv (required)
        - Required columns: 
            - record_id: uniqe id of each payment record
            - acc_id: account identifier 
            - payment_date: date of the payment
            - payment_amt: payment amount
        - Optional columns: 
            - is_auto_pay: whether the payment is a autopay, 1 for yes, 0 for no
            - is_late: whether the payment is late, 1 for yes, 0 for no

    - billing.csv (required)
        - Required columns: 
            - record_id: uniqe id of each bill record
            - acc_id: account identifier 
            - bill_date: date of the bill
            - balance: balance of the bill

    - subscription.csv (required)
        - Required columns: 
            - acc_id: account identifier 
            - subscription_date: date when the subscription happened
            - service_name: service name of the subscription

    - cost.csv (required)
        - Required columns: 
            - service_cost: average monthly cost of service use per account
            - billpay_cost: average monthly bill processing, postage and collection, and payment processing cost per account
            - upgrade_cost: average monthly expected cost of upgrades per account
            - bad_debt: average monthly estimated service bad debt per account
            - offer1_cost: average monthly estimated offer1 cost per account
        - Optional columns:
            - offer2_cost: average monthly estimated offer2 cost per account
            - offer*_cost: depending on how many items the user will provide

    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.
- Output: A list of JSON objects containing containing the predicted customer lifetime value on cust_needstate and status_change level. Reference file: sample.zip.out
    - Columns:
        - cust_needstate: Customer segmentation, it is the cluster output from use case "customer segmentation" which applied clustering techniques and provided customer cluster to identify distinct behavioral segments
        - status_change: Action segmentation, it is pre-defined segmentation to identify account status change and subscriber behavior change, e.g. account churn, add a subscription,add service 1 feature,add service 2 feature,upgrade subscription plan,downgrade subscription plan,no change,remove service 1 feature,remove service 2 feature
        - scoring_month: scoring month
        - lifetime_value: predicted lifetime value
