# Input/Output Description

- Input: A zip file containing upto 4 comma separated csv files (3 required). **__Reference file: sample.zip__**
- Details for each csv file:
    - contract.csv (required)
        - Required columns: 
            - contract_id: contract id
            - is_houseowner: is houseowner
            - vehicle_state: vehicle register state
            - checking_account_ind: checking account ind
            - number_of_years_employment: number of years with current employee
            - annual_income: annual income
            - vehicle_trade_acv_total: vehicle trade actual cash value total
            - vehicle_classification: vehicle classification
            - vehicle_type: vehicle type
            - vehicle_make: vehicle make
            - vehicle_model : vehicle model 
            - down_payment_pct: down payment pct
            - down_payment_amt: down payment amt
            - balance_payment_pct: balance payment pct
            - balance_payment_amt: balance payment amt
            - loan_amt: loan amt
            - loan_term: loan term

    - repayment.csv (required)
        - Required columns: 
            - contract_id: contract id
            - term_no: term no
            - sch_repay_dt: scheduled repayment date
            - repay_amt: repay amt
            - act_repay_dt: actual repay date
            - sys_dt: system date
            - sch_repay_amt: schedueled repayment amount

    - bureau.csv (optional)
        - optional columns(not used in model):
            - contract_id: contract id
            - month_tag: month tag
            - num_inquiries: Number of Inquiries
            - num_collections: Number of tradelines in collections status
            - ind_bankruptcy: Indicator of a Bankruptcy 
            - amt_revolving_available: Amount of Revolving Credit Available
            - oldest_trade_months: Oldest trade months
            - num_delq_tradeline_30D: The  number of Trade Lines considered 30 days Delinquent
            - num_delq_tradeline_60D: The  number of Trade Lines considered 60 days Delinquent
            - num_delq_tradeline_90d: The  number of Trade Lines considered 90 days Delinquent
            - risk_score: risk score from third-party vendor

	- collection_note.csv (required)
        - Required columns: 
            - call_date: call date
            - call_time: call time
            - current_default_days: current default days
            - history_default_times: total default times in history
            - is_callable: whether the number callable
            - is_job_stable: whether the current job stable
            - is_income_stable: whether the income stable

    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.
    
## Output
- Output: a JSON list of objects containing 'contract_id'  with original order, and one more column added named 'Score' which contains model's prediction of 30-days default in the future month likelihood scores of an current 1-day default account. **__Reference file: sample.zip.out__**

