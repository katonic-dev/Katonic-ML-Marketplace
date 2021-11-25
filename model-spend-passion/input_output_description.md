# Input/Output Description

- _Input_: A zip file containing 5 comma separated csv files. **__Reference file: sample.zip__**

Below are the details for each CSV file. 

    - **_Bureau.csv_** (*REQUIRED*): 

    | Column              | Required | Meaning                                                                                                |
    |---------------------|----------|--------------------------------------------------------------------------------------------------------|
    | acc_id              | Y        | Account ID                                                                                             |
    | month_tag           | Y        | Month tag of the monthly report                                                                        |
    | bur_bal_range_id    | Y        | Bureau Balance Range ID for the purpose of grouping account/cardholders                                |
    | auto_amt            | Y        | Indicates whether there is initial loan amount(HC/CL) of open auto loan in the last 1 month            |
    | finco_loan_bal_amt  | Y        | Finance company loan balance amount is the balance of outstanding finance company loans                |
    | hi_debt_burdn       | Y        | Highest percent debt burden for revolving/bank/national trade lines                                    |
    | max_bal_rank_nbr    | Y        | The Balance Rank with the HIGHEST Balance                                                              |
    | mort_amt            | Y        | Highest initial loan amount (HC/CL) of open mortgage                                                   |
    | mort_pay            | Y        | Average of current monthly payment amount of mort_amt                                                  |
    | opn_rvlv_bnkcrd_cnt | Y        | Number of Open BankCard Revolving Tradelines (used in ranking attributes)                              |
    | rbont_rvlv_cl_amt   | Y        | Revolving credit limit of bank; oil; and national cards                                                |
    | satis_tl_ct         | N        | SATISFACTORY-TRADE-LINE-COUNT is the count of the number of satisfactory trade lines for this prospect |
    | totl_tl_ct          | N        | TOTL-TL-CT is the total number of trade lines                                                          |
    -------------------------------------------------------------------------------------------------------------------------------------------

    - **_PNL.csv_** (*REQUIRED*): 

    | Column           | Required | Meaning                                                            |
    |------------------|----------|--------------------------------------------------------------------|
    | acc_id           | Y        | Account ID                                                         |
    | portf_id         | Y        | Portfolio ID                                                       |
    | month_tag        | Y        | Month tag of the monthly report                                    |
    | totl_credt_limit | Y        | Total credit limit                                                 |
    | interest         | Y        | Interest                                                           |
    | ca_amt           | Y        | Total dollar amount of cash advances for the current billing cycle |
    ----------------------------------------------------------------------------------------------------

    - **_Infobase.csv_** (*REQUIRED*): 
    > **Note**: Column __residence_lngth_nbr__ requires values between 00-99. Column __prem_dwelling_typ_cd__ takes (M=multiple family, S=single family)

    | Column                  | Required | Meaning                                                                                                    |
    |-------------------------|----------|------------------------------------------------------------------------------------------------------------|
    | acc_id                  | Y        | Account ID                                                                                                 |
    | month_tag               | Y        | Month tag of the monthly report                                                                            |
    | customer_id             | Y        | Customer ID                                                                                                |
    | est_resdtl_prop_own_nbr | Y        | Number of estimated investment residential properties owned by the customer                                |
    | home_pool_ind           | Y        | Indicates if the customer's home has a pool                                                                |
    | hh_property_typ_cd      | Y        | Code to represent the type of property owned by the customer                                               |
    | residence_lngth_nbr     | Y        | Indicates the total time a household has lived at their current address                                    |
    | new_mover_ind           | Y        | Indicates whether customer is a person who has moved recently into a new area                              |
    | prem_dwelling_typ_cd    | Y        | Indicates if more than one family lives at a particular address                                            |
    | home_bdrm_nbr           | Y        | Number reflecting how many bedrooms the customer's house has                                               |
    | prem_known_vehcl_cd     | Y        | Code that identifies the number of cars owned                                                              |
    | active_investor_ind     | Y        | Indicates whether the customer is an active investor or not                                                |
    | automotives_ind         | Y        | Indicates whether the customer owns an automobile                                                          |
    | cat_owner_ind           | Y        | Indicates whether the customer owns a cat                                                                  |
    | charity_int_ind         | Y        | Indicates whether the customer is interested in their community and/or charitable organizations            |
    | coins_collect_ind       | Y        | Indicates whether the customer collects coins                                                              |
    | cook_food_ind           | Y        | Indicates whether the customer is interested in cooking and food                                           |
    | crafts_int_ind          | Y        | Indicates whether the customer has an interest in crafts                                                   |
    | dog_owner_ind           | Y        | Indicates whether the customer owns a dog                                                                  |
    | elect_computer_ind      | Y        | Indicates whether the customer is interested in electronics and/or computers                               |
    | finsup_charity_ind      | Y        | Indicates that the customer financially supports charities in the community                                |
    | gold_ind                | Y        | Indicates whether the customer is interested in gold investing                                             |
    | grandchildren_ind       | Y        | Indicates that the customer is interested in grandchildren                                                 |
    | health_medcl_int_ind    | Y        | Indicates whether the customer is interested in the health and medical field                               |
    | hm_improv_ind           | Y        | Indicates whether customer is interested in home improvement                                               |
    | home_vid_record_ind     | Y        | Indicates if the customer has an interest in home video recording                                          |
    | motorcycle_ind          | Y        | Inidcates if customer is interested in motorcycles                                                         |
    | movie_music_ind         | Y        | Indicates if the customer is interested in movie music                                                     |
    | parenting_int_ind       | Y        | Indicate where the customer has interest in parenting                                                      |
    | pc_operating_sys_cd     | Y        | Code to indicate the type of PC operating system the customer owns                                         |
    | reading_ind             | Y        | Indicates whether the customer is interested in reading                                                    |
    | sew_knit_needle_ind     | Y        | Indicates whether the customer is interested in sewing and knitting or other needle activites              |
    | sports_ind              | Y        | Indicates whether the customer is interested in sports                                                     |
    | trvl_vac_cruise_tkn_ind | Y        | Indicates that the customer has taken a cruise vacation before                                             |
    | visa_reg_cc_ind         | Y        | Indicates if the customer is the user of a Visa regular credit card                                        |
    | wine_int_ind            | Y        | Indicates whether the customer is interested in wine                                                       |
    | woodwrking_ind          | Y        | Indicates whether the customer is interested in woodworking activites                                      |
    | art_antq_ord_cnt        | Y        | Count of the number of orders the household has made in the arts & antiques category in the 24 months      |
    | child_prod_ord_cnt      | Y        | Count of the number of orders the household has made in the children's products category in the 24 months  |
    | children_prod_amt       | Y        | Dollar amount the household has spent in the children's products category in the last 24 months            |
    | food_bev_amt            | Y        | Dollar amount the household has spent in the food/beverages category in the last 24 months                 |
    | general_merch_amt       | Y        | Dollar amount the household has spent in the general merchandise category in the last 24 months            |
    | genrl_apprl_amt         | Y        | Dollar amount the household has spent in the general apparel category in the last 24 months                |
    | genrl_apprl_ord_cnt     | Y        | Count of the number of orders the household has made in the general apparel category in the last 24 months |
    | gift_amt                | Y        | Dollar amount the household has spent in the gift category in the last 24 months                           |
    | hm_furnish_amt          | Y        | Dollar amount the household has spent in the home furnishings category in the last 24 months               |
    | mailord_general_ind     | Y        | Indicates that the customer has purchased mail order general products                                      |
    | pets_ord_cnt            | Y        | Count of the number of orders the household has made in the pets category in the last 24 months            |
    | prem_mail_ord_buyr_cd   | Y        | Indicates that the household has purchased products via mail in the Last 24 Months                         |
    | prem_mail_ord_resp_cd   | Y        | Indicates household has responded to a piece of collateral via mail in the last 24 months                  |
    | prem_unkn_cc_hldr_ind   | Y        | Indicates that the household has possession of an unknown type of credit card                              |
    | prm_gas_rtl_cc_hldr_ind | Y        | Indicates that the household has possession of a gas/department/retail card                                |
    | pymt_mthd_amex_cnt      | Y        | Count of the actual number of purchases made with a American Express credit card in the last 24 months     |
    | pymt_mthd_cash_cnt      | Y        | Count of the actual number of purchases made with cash in the last 24 months                               |
    | pymt_mthd_cc_cnt        | Y        | Count of the actual number of purchases made with a credit card in the last 24 months                      |
    | sport_leisure_amt       | Y        | Dollar amount the household has spent in the sports & leisure category in the last 24 months               |
    | stationery_amt          | Y        | Dollar amount the household has spent in the stationery category in the last 24 months                     |
    | stationery_ord_cnt      | Y        | Count of the number of orders the household has made in the stationery category in the last 24 months      |
    | teen_apprl_ord_cnt      | Y        | Count of the number of orders the household has made in the teen apparel category in the last 24 months    |
    | ttl_off_ord_cnt         | Y        | Count of offline orders made by the household in the last 24 months                                        |
    | ttl_off_amt             | Y        | Amount of offline orders made by the household in the last 24 months                                       |
    | avg_off_per_ord_amt     | Y        | Average dollar amount spent per offline order by the household in the last 24 months                       |
    | ttl_on_ord_cnt          | Y        | Count of online orders made by the household in the last 24 months                                         |
    | ttl_on_amt              | Y        | Amount of online orders made by the household in the last 24 months                                        |
    | avg_per_ord_amt         | Y        | Average dollar amount spent per online order by the household in the last 24 months                        |
    | uniq_retailer_cnt       | Y        | Count of the number of unique sources used in populating this record                                       |
    | upscl_dpt_cc_hldr_ind   | Y        | Indicates that the household has possession of an upscale card                                             |
    | wk_frstord_nbr          | Y        | Number of weeks since the first order in the household                                                     |
    | wk_frstord_offln_nbr    | Y        | Number of weeks since the first offline order in the household                                             |
    | wk_frstord_online_nbr   | Y        | Number of weeks since the first online order in the household                                              |
    | wk_lstord_apprl_nbr     | Y        | Number of weeks since the household has made a purchase in apparel                                         |
    | wk_lstord_furn_nbr      | Y        | Number of weeks since the household has made a purchase of furniture                                       |
    | wk_lstord_genrl_nbr     | Y        | Number of weeks since the household has made a purchase in general merchandise                             |
    | wk_lstord_gift_nbr      | Y        | Number of weeks since the household has made a purchase of a gift                                          |
    | wk_lstord_hm_furn_nbr   | Y        | Number of weeks since the household has made a purchase in home furnishings                                |
    | wk_lstord_online_nbr    | Y        | Number of weeks since the last online order in the household                                               |
    | wk_lstord_sp_gift_nbr   | Y        | Number of weeks since the household has made a purchase of a specialty gift                                |
    | wk_lstord_sprt_leis_nbr | Y        | Number of weeks since the household has made a purchase in sports and leisure                              |
    | wk_lstord_stnery_nbr    | Y        | Number of weeks since the household has made a purchase of stationery                                      |
    | wk_lstord_teen_aprl_nbr | Y        | Number of weeks since the household has made a purchase of teenager's apparel                              |
    | frst_purch_dte          | Y        | Date of the first order made by the household                                                              |
    | apprl_genrl_sc_ind      | Y        | Indicates the household made a purchase of general apparel in the last 24 months                           |
    | auto_ind                | Y        | Indicates the household made a purchase of automotive products in the last 24 months                       |
    | chldrn_genrl_decor_ind  | Y        | Indicates the household made a purchase of children's home decor/linens in the last 24 months              |
    | donation_contrib_ind    | Y        | Indicates the household made a purchase of a donation or contribution in the last 24 months                |
    | elect_comp_hmoff_sc_ind | Y        | Indicates the household made a purchase of electronics, computing & home office products in last 24 months |
    | flowers_ind             | Y        | Indicates the household made a purchase of flowers for a gift in the last 24 months                        |
    | food_beverage_sc_ind    | Y        | Indicates the household made a purchase of food/beverages in the last 24 months                            |
    | gardening_ind           | Y        | Indicates the household made a purchase of gardening products in the last 24 months                        |
    | golf_ind                | Y        | Indicates the household made a purchase of golf products in the last 24 months                             |
    | hm_furn_access_ind      | Y        | Indicates the household made a purchase of accessories in home furnishings in the last 24 months           |
    | home_garden_ind         | Y        | Indicates the household made a purchase of home & garden products in the last 24 months                    |
    | jewel_hnd_crftd_ind     | Y        | Indicates that the household has made a purchase of handcrafted/cultural jewelry within the last 24 months |
    | lifstyl_hobby_c_ind     | Y        | Indicates a purchase by the household in the last 24 months of crafts/hobbies products                     |
    | luggage_ind             | Y        | Indicates that the household has made a purchase of luggage within the last 24 months                      |
    | neural_casual_ind       | Y        | Indicates that the household has purchased men’s or women’s casual apparel in the last 24 months           |
    | neutral_access_ind      | Y        | Indicates that household has made a purchase of men's or women's accessories in apparel last 24 months     |
    | pets_ind                | Y        | Indicates that the household has made a purchase of pet products within the last 24 months                 |
    | sterl_silv_jewel_ind    | Y        | Indicates that the household has made a purchase of sterling silver jewelry within the last 24 months      |
    | young_unisx_apprl_ind   | Y        | Indicates the household made a purchase of young non-gender specific apparel in the last 24 months         | 
    ---------------------------------------------------------------------------------------------------------------------------------------------------

    - **_Scoring_date.csv_** (*REQUIRED*):

    | Column        | Required | Meaning                                       | 
    |---------------|----------|-----------------------------------------------|
    | customer_id   | Y        | Customer ID                                   |
    | scoring_date  | Y        | The date at which the category will be scored |
    ----------------------------------------------------------------------------

    - **_Transaction.csv_** (*OPTIONAL*): 
    
    | Column      | Required | Meaning                                   |
    |-------------|----------|-------------------------------------------|
    | trans_id    | Y        | Unique record ID of transaction           |
    | acc_id      | Y        | Account ID associate with the transaction |
    | customer_id | N        | Customer ID                               |
    | trans_date  | Y        | Datetime of transaction                   |
    | trans_amt   | Y        | Amount of transaction                     |
    | is_approved | Y        | Whether the transaction is approved       |
    | MCC_code    | N        | MCC code of merchant's industry           |
    ----------------------------------------------------------------------

- _Output_: a JSON list of objects contaning, with each customer's ID as the main key; for every entry, **_there up to 33_** predictions in **_33_** different columns. The **_spend_pass_prob_** contained in each column will contain the probability (passion rate) a customer is passionate about the category, respectively. **__Reference file: sample.zip.out__**

-  Categories: 
    * Beauty and Health 
    * Books and Reading-related
    * Clothing/Merchandise Expensive
    * Clothing/Merchandise
    * Coffee
    * Department Stores Expensive
    * Department 
    * Stores
    * Electronics and Appliances 
    * Entertainment 
    * Fast Food 
    * Gifts and Novelty Stores 
    * Golf 
    * Hobbies and Crafts 
    * Household Items 
    * Internet Marketplace 
    * Kids 
    * Media 
    * Pets 
    * Restaurants Expensive
    * Restaurants 
    * Sports-related 
    * Travel 
    * Travel-Cruises 
    * Wine/Liquor 
    * Auto Related Goods 
    * Drugstores and Pharmacies 
    * Furniture 
    * Groceries 
    * Home Improvement 
    * Office Supplies 
    * Telecom/Digital 
    * Wholesale Clubs

