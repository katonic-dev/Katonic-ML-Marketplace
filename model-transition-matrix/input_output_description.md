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
            - ori_fico: Origination FICO score: Borrower credit score at the time of loan issuance.
            - ori_ltv: Origination Loan-to-Value: Ratio of the outstanding loan amount at loan origination compared to original property appraisal value
            - purpose_type: A normalized code to indicate the primary reason that borrower took the mortgage.
            - doc_type: A normalized code that indicates the amount of information collected and verified at loan origination pertaining to the borrower and property. 
            - lien_type: Indicates the relative claim position on a given collateral property. 
            - prop_type: A normalized code indicates the category of collateral property against the mortgage. 
            - occ_type: Code that indicates the use of the home such as investment, second home, primary residence, etc.
            - ori_appraisal_value: Original Appraisal Value: An initial estimate of the price an asset will bear in a sale.
            - ori_intrt: Origination Interest Rate: the coupon rate charged to the borrower for the initial remittance period. It is measured in number of percentage points.
            - intrt_type: Interest Rate Type: indicator to specify  whether a loan's interest rate is fixed or adjustable.
            - prop_zip: zip code of the property
            - pmi_ind: An indicator for whether loan has a third party guarantee that principal will be repaid in the event of borrower default during the current remittance period.
            - pmicov_pct: The percentage of a loan covered by PMI in the event of a default. It is measured as a ratio of the insurance amount compared with the loan amount outstanding at the remittance period. It is measured in number of percentage points.
            - balloon_ind: Balloon Indicator: used to identify Balloon loans
            - hybridarm_ind: Hybrid Indicator: used to identify Hybrid ARM loans
            - prepaypenalty_ind: Prepay Penalty Indicator: denoting that a fee will be charged to the borrower if they elect to make unscheduled principal payments
            - optionarm_ind: Option ARM indicator: used to identify Option ARM loans
            - ios_ind: Interest Only Flag: to indicate whether the loan has a provision that allows the borrower to not repay principal but only interest on the loan for some period of time.
            - ori_intonlyterm: Interest Only Term: number of months that the borrower is allowed to only pay interest not make principal payments.
            - amortization_term: Amortization Term: term according to which monthly payments are amortizing.

    - loan_periodic.csv (required)
        - Required columns: 
            - loan_id: loan identifier
            - month_tag: Indicates the calendar month of the most current remittance period.
            - curr_remain_term: Current Remaining Term: the number of months between the most current remittance period.
            - beg_bal: Beginning Balance: Current Principal Outstanding or Unpaid Balance (UPB)
            - current_intrt: Coupon rate charged to the borrower for the most recent remittance period. It is measured in number of percentage points.
            - sched_int_amt: Scheduled Interest Amount: Interest portion of the scheduled monthly payment.
            - sched_prin_amt: Scheduled Principal amount: Principal portion of the scheduled monthly payment.

    - macroeconomics.csv (required)
        - Required columns:
            - month_tag: year month
            - TED_spread: TED Spread
            - interest_rate: interest rate

    - macroeconomics_zip.csv (required)
        - Required columns:
            - month_tag: year month
            - zip: zip code
            - HPI: home price indice on zip code level
            - unemployment_rate: unemployment rate


## Output
- Output: a JSON list of objects the probability of a loan ending up in a certain status in the next month.
    - Columns:
        - loan_id: loan identifer
        - p_cc: probability from current to current. Loan remains current
        - p_cq1: probability from current to 30 days past due. Becomes one-month delinquent
        - p_cp: probability from current to prepayment. Prepays
        - p_q1c: probability from 30 days pas due to current. Loan cures delinquency
        - p_q1q1: probability from 30 days pas due to 30 days pas due. Stays one-month delinquent
        - p_q1q2: probability from 30 days pas due to 60+ days pas due. Misses another payment
        - p_q1p: probability from 30 days pas due to prepayment. Prepays 
        - p_q2c: probability from 60+ days pas due to current. Loan cures
        - p_q2q1: probability from 60+ days pas due to 30 days pas due. Partial cure
        - p_q2q2: probability from 60+ days pas due to 60+ days pas due. Remains delinquent
        - p_q2d: probability from 60+ days pas due to non-liquidation defaults. Defaults
        - p_dc: probability from non-liquidation defaults to current. Cures due to loan modification
        - p_dd: probability from non-liquidation defaults to non-liquidation defaults. Remains in default queue awaiting liquidation
        - p_dl: probability from non-liquidation defaults to liquidation. Liquidates

**__Reference file: sample.zip.out__**
