# Input/Output Description

- Input: A zip file containing upto 7 comma separated csv files. Reference file: sample.zip
- Details for each csv file:
    - **_usage_history.csv_** (*REQUIRED*): Table containing usage history for each customer on dimensions of data, voice, and sms.

    | Column                          | Required         | Meaning                                                                                                                                                                                                                                 |
    |---------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | ACCOUNT_ID                      | Y                | Billing account number (BAN)                                                                                                                                                                                                            |
    | SUB_ID                          | Y                | Subscriber ID                                                                                                                                                                                                                           |
    | DATA_USAGE_AMT                  | Y                | Subscriber SOCs data usage for the previous billing cycle closed during the month ending on the report date, excluding taxes.                                                                                               |
    | DATA_ADDED_SERVICES_AMT    | Y                | Add-on SOCs for the billing cycle.                                                                                                       |
    | DATA_OVERAGE_AMT           | Y                | Megabyte overage for the billing cycle.                                                                                                       |
    | DATA_ROAM_AMT              | Y                | Megabyte usage while roaming outside of the home calling area for the billing cycle.                                                          |
    | DATA_PREMIUM_SERVICE_AMT   | Y                | Premium content download use.                                                                |
    | MMS_ADDED_SERVICES_AMT     | Y                | Add-on MMS only SOCs.                                                                                                   |
    | MMS_OVERAGE_AMT            | Y                | MMS use overage.                                                                                                        |
    | VOICE_USAGE        | Y                | Voice SOC minutes.                                                                                                    |
    | VOICE_ADDED_SERVICES_AMT   | Y                | Add on voice SOCs.                                                                                                      |
    | VOICE_OVERAGE_AMT          | Y                | Voice minute overage.                                                                                           |
    | VOICE_TOLL_AMT             | Y                | Minutes used dialing outside of the home calling area.                                                                  |
    | VOICE_ROAM_AMT             | Y                | Minutes used while roaming outside of the home calling area.                                                            |
    | SMS_AMT          | Y                | SMS SOCs.                                                                                                |
    | SMS_ADDED_SERVICES_AMT     | Y                | Add on SMS or SMS and MMS bundle SOCs.                                                                                  |
    | SMS_OVERAGE_AMT            | Y                | SMS use overage.                                                                                                        |
    | SMS_ROAM_AMT               | Y                | SMS or MMS used while roaming outside of the home calling area.                                                         |
    | OTHER_AMT                  | N                | Other usages/charges                                                                                                                                                                                                                     |
    

    - **_voice_call_transaction.csv_** (*REQUIRED*): Monthly Voice Usage for each Customer.

    | Column                            | Required | Meaning                                  |
    |-----------------------------------|----------|------------------------------------------|
    | ACCOUNT_ID                        | Y        | Account ID                               |
    | SUB_ID                            | Y        | Subscriber ID                            |
    | CALL_DATE                         | Y        | Call date                                |
    | ROAMING_IND                       | Y        | Indicator of roaming                     |
    | OUTBOUND_IND                      | Y        | Indicator of outbound call               |
    | ITNL_IND                          | Y        | Indicator of international call          |
    | TOTAL_ANSWERED_CALLS              | Y        | Total number of answered calls           |
    | TOTAL_DROPPED_CALLS               | Y        | Total number of dropped calls            |
    | TOTAL_CALLS                       | Y        | Total number of calls                    |
    | TOTAL_CALL_DURATION_IN_MINUTE     | Y        | Total call duration in minute            |
    | ANSWERED_CALL_DURATION_IN_MINUTE  | Y        | Total answered call duration in minute   |
    
    
    - **_data_service_transaction.csv_** (*REQUIRED*): Monthly Data Usage for each Customer.

    | Column                | Required | Meaning                                  |
    |-----------------------|----------|------------------------------------------|
    | ACCOUNT_ID            | Y        | Account ID                               |
    | SUB_ID                | Y        | Subscriber ID                            |
    | TRANSACTION_DATE      | Y        | Transaction date                         |
    | NETWORK_TECHNOLOGY    | Y        | The network technology                   |
    | ROAMING_IND           | Y        | Indicator of roaming                     |
    | INTL_IND              | Y        | Indicator of international data session  |
    | NUM_OF_SESSIONS       | Y        | Number of sessions                       |
    | METERED_DATA_USAGE    | Y        | Metered data usage                       |
    | UNMETERED_DATA_USAGE  | Y        | Unmetered data usage                     |
    | TOTAL_USAGE           | Y        | Total data usage                         |
    | NETWORK_CARRIER       | N        | Network carrier                          |

    - **_sms_service.csv_** (*REQUIRED*): Monthly SMS Usage for each Customer.
    
    | Column            | Required | Meaning                        |
    |-------------------|----------|--------------------------------|
    | ACCOUNT_ID        | Y        | Account ID                     |
    | SUB_ID            | Y        | Subscriber ID                  |
    | DATA_DATE         | Y        | Data date                      |
    | OUTBOUND_IND      | Y        | Indicator of outbound SMS      |
    | SMS_TYPE_CODE     | Y        | SMS type code                  |
    | INTERCARRIER_IND  | Y        | Indicator of intercarrier SMS  |
    | TOTAL_MSG_COUNT   | Y        | Total SMS count                |
    
    
    - **_device_history.csv_** (*OPTIONAL*): Monthly Device Usage for each Customer.

    | Column              | Required | Meaning                                                          |
    |---------------------|----------|------------------------------------------------------------------|
    | SUB_ID              | Y        | Subscriber ID                                                    |
    | ACCOUNT_ID          | Y        | Account ID                                                       |
    | ORDER_IND           | Y        | Order indicator                                                  |
    | RETURN_IND          | Y        | Return indicator                                                 |
    | NEW_ACT_IND         | Y        | New activated handset indicator                                  |
    | UPGRADE_IND         | Y        | Upgrade indicator                                                |
    | TXN_DT              | Y        | Transaction date                                                 |
    | PLAN_TYPE_CD        | N        | Plan type code                                                   |
    | SKU_MODEL           | N        | Stock Keeping Unit Model                                         |
    | SKU_MAKE            | N        | Stock Keeping Unit manufacture                                   |
    | SUB_START_DT        | Y        | The date the subscriber starts to use handset                    |
    | PRICE_AMT           | Y        | Handset price                                                    |
    | DISCOUNT_AMT        | N        | Discount amount                                                  |
    | COST_AMT            | N        | Cost amount                                                      |
    | IMEI(IMEI_14)       | Y        | The International Mobile Equipment Identity                      |
    | EIP_IND             | N        | Indicates that the customer is on an equipment installment plan  |
    | FIRST_USE_NETWK_DT  | N        | The network date of first usage                                  |
    | SIM_DEVICE_IND      | N        | Indicator of device using SIM card                               |
    
    - **_memo.csv_** (*OPTIONAL*): Monthly memos for each Customer. This refers to notes during customer service calls.

    | Column              | Required | Meaning                |
    |---------------------|----------|------------------------|
    | OPERATOR_ID         | Y        | Operator ID            |
    | CREATED_DATE_TIME   | N        | Create date time       |
    | MODIFIED_DATE_TIME  | N        | Modified date time     |
    | ACCOUNT_ID          | Y        | Account ID             |
    | MEMO_ID             | Y        | Memo ID                |
    | MEMO_DATE_TIME      | Y        | Memo datetime          |
    | MEMO_TYPE_CODE      | Y        | Memo type code         |
    | SUB_ID              | Y        | subscriber ID          |
    | SYSTEM_TEXT         | Y        | System generated text  |
    | MANUAL_TEXT         | Y        | Manually entered text  |
    
    - **_subscription_status.csv_** (*OPTIONAL*): Subscriptions for each Customer.
    
    | Column                       | Required | Meaning                      |
    |------------------------------|----------|------------------------------|
    | ACCOUNT_ID                   | Y        | Account ID                   |
    | SUB_ID                       | Y        | Subscriber ID                |
    | ACTIVATION_DATE              | Y        | Activation date              |
    | SUBSCRIBER_STATUS_TYPE_CODE  | Y        | Subscriber status type code  |
    | LAST_STATUS_UPDATE_DATE      | Y        | Last status update date      |
    
- Output: a JSON list of objects contaning all the 'ACCOUNT_ID' and "SUB_ID" in the input, with one more column added named 'PREDICTED_DATA_GB' which contains model's prediction of the monthly data usage for the customer.
