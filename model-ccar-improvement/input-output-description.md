## Input Files

> **Note**: The customer should provide the following formatted data in 2 CSV files. The files should zipped into a single file e.g. input.zip
- Input: 2 comma separated csv (2 required)
- Details for each csv file:
    - Loan.csv (required)
        - Required columns: 
            - loan_id: Unique Loan Identification Number
            - loan_term: Loan Term
            - vintage_month: vintage month
            - vintage_quart: vintage quarterly
            - mob: Months on Book (number of months since booking)
            - perf_month: Performance Month / Calendar Month
            - loan_rate: Loan APR
            - loan_size: Loan Origination Amount
            - schd_tot_pymt: Contractual Scheduled Total Payment
            - act_prin_pymt: Actual Principle Payment 
            - act_beg_bal: Actual Beginning Principal Balance
            - act_end_bal: Actual Ending Principal Balance

    - Macroeconomics.csv (required)
        - Required columns: 
            - perf_month: Year Month
            - Unemployment_Initial_Claim: Unemployment Initial Claims

    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.

## Output
- Output: a json response containing the predicted ending balance for the portfolio under non-stressed and stressed economic conditions of each performance month.


