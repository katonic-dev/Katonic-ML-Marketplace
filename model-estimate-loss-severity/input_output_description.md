# Input/Output Description

- Input: A zip file containing 4 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - loan.csv (required)
        - Required columns: 
            - loan_id: An unique identify for each loan.
            - ori_issue_date: Origination Date: The date that the loan was issued. 
            - ori_maturity_date: Maturity Date: The date the loan was expected to mature.
            - sector_cd: Category that describes underwriting program, credit quality, etc.
            - ori_bal: Original Balance: The original principal outstanding at mortgage origination date. 
            - purpose_type: A normalized code to indicate the primary reason that borrower took the mortgage.
            - doc_type: A normalized code that indicates the amount of information collected and verified at loan origination pertaining to the borrower and property.
            - prop_type: A normalized code indicates the category of collateral property against the mortgage. 
            - occ_type: Code that indicates the use of the home such as investment, second home, primary residence, etc.
            - ori_appraisal_value: Original Appraisal Value: An initial estimate of the price an asset will bear in a sale.
            - ori_intrt: Origination Interest Rate: the coupon rate charged to the borrower for the initial remittance period. It is measured in number of percentage points.
            - intrt_type: Interest Rate Type: indicator to specify  whether a loan's interest rate is fixed or adjustable.
            - prop_zip: zip code of the property
            - pmi_ind: An indicator for whether loan has a third party guarantee that principal will be repaid in the event of borrower default during the current remittance period.
            - pmicov_pct: The percentage of a loan covered by PMI in the event of a default. It is measured as a ratio of the insurance amount compared with the loan amount outstanding at the remittance period. It is measured in number of percentage points.
            - amortization_term: Amortization Term: term according to which monthly payments are amortizing. 

    - loan_periodic.csv (required)
        - Required columns: 
            - loan_id: loan identifier
            - month_tag: Indicates the calendar month of the most current remittance period.
            - curr_remain_term: Current Remaining Term: the number of months between the most current remittance period.
            - beg_bal: Beginning Balance: Current Principal Outstanding or Unpaid Balance (UPB)
            - current_intrt: Coupon rate charged to the borrower for the most recent remittance period. It is measured in number of percentage points.
            - sched_prin_amt: Scheduled Principal amount: Principal portion of the scheduled monthly payment.

    - macroeconomics.csv (required)
        - Required columns:
            - month_tag: year month
            - interest_rate: interest rate

    - macroeconomics_zip.csv (required)
        - Required columns:
            - month_tag: year month
            - zip: zip code
            - HPI: home price indice on zip code level

    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.

## Output
- Output: a JSON list of objects containing the predicted loss severities for residential mortgages.
    - Columns:
        - loan_id: loan identifer
        - loss_severity: predicted loss severity for the loan
        
**__Reference file: sample.zip.out__**
