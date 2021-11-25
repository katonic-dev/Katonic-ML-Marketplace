# Input/Output Description

- Input: A zip file containing 2 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - application.csv (required)
        - Required columns: 
            - acc_id: Account ID
            - app_date: application date
            - income: total annual gross income
            - balcon_amt: balance transfer amount requested
            - product_cd: portfolio id, product type


    - bureau.csv (required)
        - Required columns: 
            - acc_id: Account ID
            - month_tag: Year Month
            - risk_score: risk score from 3rd party, e.g. FICO score 
            - debt_burden: Total average debt burden
            - ratio_bal_line_6mth: Overall balance to credit limit ratio on open revolving trades reported in the last 6 months 
            - avg_bal_24mth_trans: Average Balance for 24-month Transacting Trade lines
            - tol_bal_6mth: Total balance on open credit card trades reported in the last 6 months 
            - tol_credit_6mth: Total credit amount on open revolving trades reported in the last 6 months 
            - tol_pay_xmort: Total monthly installment payments excluding mortgage
            - nbr_bkcrd_util_6mth: The number of bankcard trades with utilization within the last 6 months.
            - totl_tl_ct_12mth: Total number of trade lines in the last 12mth
            - nbr_accounts: Number of Open Accounts
            - 2nd_hi_opn_rev_util: The 2nd highest utilization on open revolving trades
            - tol_lmt_tr_amt: Total limit on all bankcard trades
            - totl_tl_ct_24mth: Total number of trade lines in the last 24mth
            - tol_plast_cnt: Total number of cards to issue.
            - nbr_open_trade_6mth: Total number of open trades presently satisfactory reported in the last 6 months  
            - nbr_instl_trade: Total number of installment trades  
            - nbr_trade_gr0_util_9mth: Number of trades with > 0%  utilization change within 9 months
            - major_delnq_ct: Number of major delinquencies.
            - rbont_rvlv_cl_amt: Revolving credit limit of bank; oil; and national cards
            - hi_debt_burdn_pct: Highest percent debt burden for revolving/bank/national trade lines
            - totl_rvlv_bal_amt: Total Revolving Balance of Open Bank/Finance/Natl/Retail/Oil Trades
            - totl_bal_amt: Total dollar balance at the time of the balance control activity.
            - totl_bnkcrd_cl_amt: Aggregate revolving bankcard credit limit.
            - totl_mortg_bal_amt: Total balance of mortgage
            - opn_rvlv_bnkcrd_cnt: Number of Open BankCard Revolving Tradelines (used in ranking arrtibutes)
            - delnq_bankcard_month_age: months since most recent delinquency for Bankcard trades
            - hi_delnq_bankcard_12m: Highest delinquency on any bank revolving trade line in the last 12 months.


## Output
- Output: a JSON list of objects containing the optimal initial credit line for each applicant.
    - Fields:
        - acc_id: Account ID
        - init_line: Recommended initial credit line for the account

**__Reference file: sample.zip.out__**
