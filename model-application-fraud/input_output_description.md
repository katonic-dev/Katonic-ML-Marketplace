# Input/Output Description

- Input: A zip file containing 5 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - application.csv (required)
        - Required columns: 
            - application_id: application id
            - application_date: application date
            - checking_account_ind: Checking Account Indicator
            - is_houseowner: is houseowner
            - vehicle_using_state: vehicle using state
            - working_years: working years
            - yearly_income: yearly income(10K)
            - vehicle_trade_acv_total: The Actual Cash Value of the Traded in Vehicle
            - vehicle_production: vehicle production type
            - vehicle_make: vehicle make
            - vehicle_model : vehicle model
            - vehicle_type: new or secondhand
            - down_payment_pct: down-payment pct
            - down_payment_amt: down-payment amt
            - balance_payment_pct: balance-payment pct
            - balance_payment_amt: balance-payment amt
            - loan_amt: total loan amt, including other costs
            - loan_term: loan term
            - apply_channel: which app applicants used
            - apply_period: how long to finish the application
            - contact1_relation: relation with contact 1
            - contact2_relation: relation with contact 2
            - contact1_phone_number: mobile number of contact 1
            - contact2_phone_number: mobile number of contact 2
            - contract_id: contract id

    - repayment.csv (required)
        - Required columns: 
            - contract_id: contract id
            - term_no: term no
            - sch_repay_dt: scheduled repayment date
            - repay_amt: repay amt
            - act_repay_dt: actual repay date
            - sys_dt: system date
            - sch_repay_amt: schedueled repayment amount

    - credit_report.csv (required)
        - Required columns:
            - application_id: application id
            - num_inquiries: Number of Inquiries
            - num_collections: Number of tradelines in collections status
            - ind_bankruptcy: Indicator of Bankruptcy 
            - amt_revolving_available: Amount of Revolving Credit Available
            - oldest_trade_months: Oldest trade months
            - applicant_multiloan_7days: indicator of applicant applied for multiloan in last 7days
            - applicant_multiloan_1mon: indicator of applicant applied for multiloan in last 1 month
            - applicant_multiloan_3mons: indicator of applicant applied for multiloan in last 3 months

    - fraud_verification.csv (required)
        - Required columns:			
            - application_id: application id
            - applicant_name_id_phone_verify: applicant name id phone verify
            - applicant_mobile_status: applicant mobile status
            - applicant_mobile_useyears: applicant mobile useyears
            - ind_fraud_applicant_mobile: whether applicant's mobile number matches the fraud list
            - ind_fraud_applicant_id: whether applicant's id matches the fraud list
            - ind_fraud_applicant_company: whether applicant's company matches the fraud list
            - ind_fraud_contact1_mobile: whether contact1's mobile number matches the fraud list
            - ind_fraud_contact2_mobile: whether contact2's mobile number matches the fraud list
			
	- collection_note.csv (required)
        - Required columns: 
            - call_date: call date
            - call_time: call time
            - current_default_days: current default days
            - history_default_times: total default times in history
            - is_callable: whether the number callable
            - is_job_stable: whether the current job stable
            - is_income_stable: whether the income stable
            
## Output
- Output: a JSON list of objects containing 'application_id'  with original order, and one more column added named 'Score' which contains model's prediction of application fraud during first three terms in Auto Loan industry. **__Reference file: sample.zip.out__**

