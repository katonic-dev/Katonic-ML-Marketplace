# Input/Output Description

- Input: A zip file containing 9 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - **_billing_history.csv_** (*REQUIRED*): 

    | Column                          | Required         | Meaning                                                                                                                                                                                                                                 |
    |---------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | ACCOUNT_ID                      | Y                | Billing account number (BAN)                                                                                                                                                                                                            |
    | SUB_ID                          | Y                | Subscriber ID                                                                                                                                                                                                                           |
    | BILL_CYCLE_ID                   | Y                | Bill cycle ID of account (1-31)                                                                                                                                                                                                         |
    | BILL_CYCLE_START_DATE           | Y                | Starting date of the bill cycle that ends within report date calendar month                                                                                                                                                             |
    | BILL_CYCLE_CLOSE_DATE           | Y                | Closing date of the bill cycle that ends within report date calendar month                                                                                                                                                              |
    | BILL_CYCLE_PMT_DUE_DATE         | Y                | Payment due date of bill cycle                                                                                                                                                                                                          |
    | DATA_RATE_PLAN_CHRG_AMT         | Y                | Subscriber billing for data only rate plan SOCs for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                               |
    | DATA_ADDED_SERVICES_CHRG_AMT    | Y                | Subscriber billing for add-on data SOC for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                        |
    | DATA_OVERAGE_CHRG_AMT           | Y                | Subscriber billing for megabyte overage for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                       |
    | DATA_ROAM_CHRG_AMT              | Y                | Subscriber billing for megabyte usage while roaming outside of the home calling area for the billing cycle closed during the month ending on the report date, excluding taxes.                                                          |
    | DATA_PREMIUM_SERVICE_CHRG_AMT   | Y                | Subscriber billing for premium content download use (excluding COGA downloads) for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                |
    | MMS_ADDED_SERVICES_CHRG_AMT     | Y                | Subscriber billing for add-on MMS only SOCs for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                   |
    | MMS_OVERAGE_CHRG_AMT            | Y                | Subscriber billing for MMS use overage for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                        |
    | VOICE_RATE_PLAN_CHRG_AMT        | Y                | Subscriber billing for voice rate plan SOC for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                    |
    | VOICE_ADDED_SERVICES_CHRG_AMT   | Y                | Subscriber billing for add on voice SOCs for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                      |
    | VOICE_OVERAGE_CHRG_AMT          | Y                | Subscriber billing for voice minute overage charges for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                           |
    | VOICE_TOLL_CHRG_AMT             | Y                | Subscriber billing for minutes used dialing outside of the home calling area for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                  |
    | VOICE_ROAM_CHRG_AMT             | Y                | Subscriber billing for minutes used while roaming outside of the home calling area for the billing cycle closed during the month ending on the report date, excluding taxes.                                                            |
    | SUB_ACT_CHRG_AMT                | Y                | Subscriber billing for current period subscriber activations on the Subscriber                                                                                                                                                          |
    | SMS_RATE_PLAN_CHRG_AMT          | Y                | Subscriber billing for SMS only rate plan SOCs for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                |
    | SMS_ADDED_SERVICES_CHRG_AMT     | Y                | Subscriber billing for add on SMS or SMS and MMS bundle SOCs for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                  |
    | SMS_OVERAGE_CHRG_AMT            | Y                | Subscriber billing for SMS use overage for the billing cycle closed during the month ending on the report date, excluding taxes.                                                                                                        |
    | SMS_ROAM_CHRG_AMT               | Y                | Subscriber billing for SMS or MMS used while roaming outside of the home calling area for the billing cycle closed during the month ending on the report date, excluding taxes.                                                         |
    | SUB_EARLY_TERMINATION_CHRG_AMT  | Y                | Subscriber billing for early termination on the Subscriber                                                                                                                                                                              |
    | SUB_HANDSET_CHRG_AMT            | N                | Subscriber billing item for equipment charges that were billed to the Subscriber for the billing cycle closed during the month ending on the report date, excluding taxes. This amount does NOT include equipment purchased in stores.  |
    | OTHER_CHRG_AMT                  | N                | Other charge amount                                                                                                                                                                                                                     |
    | ADJUSTMENT_BILL_CYCLE_AMT       | Y                | Adjustment amount for the billing cycle closed                                                                                                                                                                                          |
    | ACTUAL_REVENUE_BILL_CYCLE_AMT   | Y                | Actual revenue amount of current bill cycle                                                                                                                                                                                             |
    

    - **_voice_call_transaction.csv_** (*REQUIRED*): 

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
    
    
    - **_data_service_transaction.csv_** (*REQUIRED*): 

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
    
    
    - **_device_history.csv_** (*REQUIRED*): 

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
    
    - **_memo.csv_** (*REQUIRED*): 

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
    
    
    - **_payment_history.csv_** (*REQUIRED*): 

    | Column                   | Required | Meaning                  |
    |--------------------------|----------|--------------------------|
    | ACCOUNT_ID               | Y        | Account ID               |
    | SUB_ID                   | Y        | Subscriber ID            |
    | PAYMENT_SEQUENCE_NUMBER  | Y        | Payment Sequence number  |
    | DEPOSIT_DATE             | Y        | Deposit Date             |
    | PAYMENT_METHOD_CODE      | Y        | Payment method code      |
    | AMOUNT_DUE               | Y        | Amount due               |
    | RECEIPT_ID               | Y        | Receipt ID               |
    | PAYMENT_ACTIVITY_DATE    | Y        | Payment activity date    |
    | PAYMENT_ACTIVITY_AMOUNT  | Y        | Payment activity amount  |
    
    - **_rateplan_history.csv_** (*REQUIRED*): 
    
    | Column                          | Required | Meaning                         |
    |---------------------------------|----------|---------------------------------|
    | SOC_ID                          | Y        | SOC ID                          |
    | ACCOUNT_ID                      | Y        | Account ID                      |
    | SUB_ID                          | Y        | Subscriber ID                   |
    | SUBSCRIBER_SOC_EFFECTIVE_DATE   | Y        | Subscriber SOC effective date   |
    | SUBSCRIBER_SOC_EXPIRATION_DATE  | Y        | Subscriber SOC expiration date  |
    | SOC_RATE_AMOUNT                 | Y        | SOC rate amount                 |
    | CREATED_DATE_TIME               | Y        | Created datetime                |
    | MODIFIED_DATE_TIME              | Y        | Modified datetime               |
    
    - **_sms_service.csv_** (*REQUIRED*): 
    
    | Column            | Required | Meaning                        |
    |-------------------|----------|--------------------------------|
    | ACCOUNT_ID        | Y        | Account ID                     |
    | SUB_ID            | Y        | Subscriber ID                  |
    | DATA_DATE         | Y        | Data date                      |
    | OUTBOUND_IND      | Y        | Indicator of outbound SMS      |
    | SMS_TYPE_CODE     | Y        | SMS type code                  |
    | INTERCARRIER_IND  | Y        | Indicator of intercarrier SMS  |
    | TOTAL_MSG_COUNT   | Y        | Total SMS count                |
    
    - **_subscription_status.csv_** (*REQUIRED*): 
    
    | Column                       | Required | Meaning                      |
    |------------------------------|----------|------------------------------|
    | ACCOUNT_ID                   | Y        | Account ID                   |
    | SUB_ID                       | Y        | Subscriber ID                |
    | ACTIVATION_DATE              | Y        | Activation date              |
    | SUBSCRIBER_STATUS_TYPE_CODE  | Y        | Subscriber status type code  |
    | LAST_STATUS_UPDATE_DATE      | Y        | Last status update date      |
    
## Output
- Output: a JSON list of objects containing all the 'ACCOUNT_ID' in the input, with one more column added named 'SCORE' which contains model's prediction of the a telecom account's probability to add a voice line in telecom industry **__Reference file: sample.zip.out__**
