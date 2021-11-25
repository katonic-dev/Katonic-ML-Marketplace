## Input
Supported content types:  text/csv

## Input Details:
## Input: More than 5 comma separated csv (depending on how many service usage provided)

## Details for each csv file:

### scoring_date.csv (required)

Required columns:
```
scoring_date: scoring date for caculating signals and generate master table, format 'YYYY-MM-DD', eg: '2020-08-01'
```

### profile.csv (required)

Required columns:
```
accountID: Contact's accountID
avg_service_tenure: average tenure of services that the account used
tenure: tenure
num_service: number of services that the account is using
num_past_churn: number of churn happened to this account in history
churn_ind: churn indicator
```

### bill_records.csv (required)

Required columns: 
```
recordID: unique id of each bill record
accountID: Contact's accountID
bill_date: Date of the bill, format: 'YYYY-MM-DD' eg: '2018-07-07'
balance: balance of the bill
```

### payment_records.csv (required)

Required columns: 
```
recordID: unique id of each payment record
accountID: Contact's accountID
payment_time: Date of the payment record of the contact, format: 'YYYY-MM-DD hh:mm:ss' eg: '2018-07-07 12:09:32'
amount: amout of payment
is_auto_pay: whether the payment is a autopay, 1 for yes, 0 for no
is_late: whether the payment is late, 1 for yes, 0 for no
```

### service1_usage_records.csv (required)**

Required columns:
```
recordID: unique id of each payment record
accountID: Contact's accountID
record_time: Date of the service usage record of the contact, format: 'YYYY-MM-DD hh:mm:ss' eg: '2018-07-07 12:09:32'
amount: usage amout of service
** service1 means the primary service provided to customer
```

### serviceN_usage_records.csv (optional, N=2,3,4,5...**)

Required columns:
```
recordID: unique id of each payment record
accountID: Contact's accountID
record_time: Date of the service usage record of the contact, format: 'YYYY-MM-DD hh:mm:ss' eg: '2018-07-07 12:09:32'
amount: usage amout of service
**N=2,3,4,5,6,7...., can add any number of service usage table, follow the same schema of service1_usage_records.csv
```

### subscription_records.csv (optional)

Required columns:
```
recordID: unique id of each subscription record
accountID: Contact's accountID
subscription_date: Date of the subscription record of the contact, format: 'YYYY-MM-DD' eg: '2018-07-07'
service: the service that the contact subscribed to.
```

NOTE:  Only tar and tar.gz compression formats supported.
