## Input Files

> **Note**: The customer should provide the following formatted data in CSV files. The files should then be archived and zipped into a single file e.g. input.tar.gz 

- Input: 3 comma separated csv
- Details for each csv file:
    - authorization_fraud.csv (required)
        - Required columns:
            - card_nbr: Account #
            - credit_debit_ind: Credit-Sig Debit Ind
            - expiration_date: Expiration Date (only with hashed PAN)
            - acct_prefix6: Hashed  BIN to identify issuer, and hashed Roll-up to parent BIN identifying as parent.
            - card_avs_ind: Cardholder ADDR VERIFY SERVICE(AVS) indicator
            - banknet_date: transaction date
            - banknet_time: transaction TimeStamp
            - txn_usd_amt: transaction Amount
            - merch_category_cd: Merchant Category code
            - merch_id: Merchant ID (Card Acceptor ID Code),used to derive mid_zip5
            - card_present_cd: Card present code
            - pan_entry_mode_cd: Transaction keyed/swiped
            - auth_response_action: Auth decision
            - network_cd: Processor or network switch identification 
            - attendance_ind: attendance indicator
            - cardholder_present_cd: cardholder present flag
            - pos_country_cd: Point of sale Country Code, e.g."840" means USA
            - pos_postal_cd: Point of Postal Code, used to derive zip5
            - transaction_dttm: TRANSACTION_DTTM,merge key with fraud_claims
            - audit_control_num: AUDIT_CONTROL_NUM,merge key with fraud_claims
            - issuer_id: ISSUER_ID,merge key with fraud_claims
        - Optional columns:
            - industry_code: Industry ID code
            - merch_name: Merchant Name 
            - merch_city: Merchant City
            - merch_state: Merchant State

    - authorization_nonfraud.csv (required)
        - Required columns:
            - card_nbr: Account # 
            - credit_debit_ind: Credit-Sig Debit Ind
            - expiration_date: Expiration Date (only with hashed PAN)
            - acct_prefix6: Hashed  BIN to identify issuer, and hashed Roll-up to parent BIN identifying as parent.
            - card_avs_ind: Cardholder ADDR VERIFY SERVICE(AVS) indicator
            - banknet_date: Date
            - banknet_time: TimeStamp
            - txn_usd_amt: transaction Amount
            - merch_category_cd: Merchant Category code
            - merch_id: Merchant ID (Card Acceptor ID Code),used to derive mid_zip5
            - card_present_cd: Card present code
            - pan_entry_mode_cd: Transaction keyed/swiped
            - auth_response_action: Auth decision
            - network_cd: Processor or network switch identification 
            - attendance_ind: attendance indicator
            - cardholder_present_cd: cardholder present flag
            - pos_country_cd: Point of sale Country Code, e.g."840" means USA
            - pos_postal_cd: Point of sale Postal Code, used to derive zip5
        - Optional columns:
            - industry_code: Industry ID code
            - merch_name: Merchant Name 
            - merch_city: Merchant City
            - merch_state: Merchant State
            - transaction_dttm: Empty for authorization_nonfraud
            - audit_control_num: Empty for authorization_nonfraud
            - issuer_id: Empty for authorization_nonfraud

    - fraud_claims.csv (required)
        - Required columns: 
            - card_nbr: Account #,merge key with authorization file
            - fraud_type_cd: fraud type code
            - transaction_dttm: TRANSACTION_DTTM,merge key with authorization file
            - audit_control_num: AUDIT_CONTROL_NUM, merge key with authorization file
            - issuer_id: ISSUER_ID, merge key with authorization file
            - fraud_rpt_dt: Fraud date cardholder reported fraud to issuer
            - entered_dttm: Fraud entered date into fraud_claims

    - Note: if end user do not have optional columns, a column with all missing values shoud be placed.

## Output
- A json response containing 'mid_zip5' with original order, and one more column added named 'score' which contains model's prediction of the compromise score for the record.
