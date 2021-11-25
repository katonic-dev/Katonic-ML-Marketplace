# Input/Output Description

## Input:
A **zip file** with the following comma separated csv files. Reference file: sample.zip

- **_Bureau.csv_** (*REQUIRED*): 


| Column              | Required | Meaning                                                             |
|---------------------|----------|---------------------------------------------------------------------|
| acc_id              | Y        | Account's unique ID                                                 |
| month_tag           | Y        | Month tag of the monthly report                                     |
| hi_debt_burdn       | Y        | Highest percent debt burden for revolving/bank/national trade lines |
| fico_score          | Y        | Customer's fico score                                               |
| age_tl_ct           | Y        | Age of oldest trade lines                                           |
| avg_opn_bnkcrd      | Y        | Average age of open bank cards                                      |
| bankr_ind           | Y        | Indicate if any bankruptcies                                        |
| totl_opn_tl         | Y        | Total number of opened trade lines                                  |
| opn_rvlv_bnkcrd_cnt | Y        | Number of open bank card revolving tradelines                       |
| rbont_rvlv_cl_amt   | Y        | Revolving credit limit of bank; oil; and national cards             |
| low_cl_limit        | Y        | Lowest credit limit on open bank card                               |
| opn_tl_months       | Y        | Months since most recently opened trade line                        |
| hi_bnkcrd_util      | Y        | Highest utilization of revolving bank card trades                   |
| totl_bnkcrd_util    | Y        | Total number of bank revolving trades with utilization              |
| totl_tl_ct          | Y        | Total number of trade lines                                         |
--------------------------------------------------------------------------------------------------------

- **_PNL.csv_** (*REQUIRED*): 

| Column           | Required | Meaning                                                                                                     |
|------------------|----------|-------------------------------------------------------------------------------------------------------------|
| acc_id           | Y        | Account's unique ID                                                                                         |
| month_tag        | Y        | Month tag of the monthly report                                                                             |
| totl_credt_limit | Y        | Total credit limit                                                                                          |
| credt_interest   | Y        | Interest                                                                                                    |
| ca_amt           | Y        | Total dollar amount of cash advances for the current billing cycle                                          |
| credt_bal        | Y        | Credit card balance for the month                                                                           |
| min_pay          | Y        | Min Payment Amount                                                                                          |
| credt_fee        | Y        | Type of credit card fee (i.e. Balance Transfer, Cash Advance, Expedited Payment, etc. and "None" if no fee) |
| delinq_lvl       | Y        | Delinquency level (i.e. 30 days, 60 days, etc. and "None" if no delinquency level)                          |
---------------------------------------------------------------------------------------------------------------------------------------------

- **_Campaign_Mail.csv_** (*REQUIRED*): 

| Column         | Required | Meaning                                               |
|----------------|----------|-------------------------------------------------------|
| prospect_id    | Y        | Prospect ID of who was sent the direct mail           |
| acc_id         | Y        | Account's unique ID                                   |
| mail_sent_date | Y        | Date mail or remail was sent                          |
| last_mail_days | Y        | Number of days since last mail was sent               |
| program_name   | Y        | Name of program                                       |
| program_dur    | Y        | Program duration                                      |
| program_prod   | Y        | Product or offer in program                           |
| program_apr    | Y        | Product's APR (if not applicable then enter "None")   |
| resp_chann     | Y        | Response channel (what prospect used to respond)      |
| resp_date      | Y        | Response date                                         |
| status_date    | Y        | Approve/Decline Date                                  |
-------------------------------------------------------------------------------------

- **_Infobase.csv_** (*OPTIONAL*): 

| Column                    | Required | Meaning                                                                                                               |
|---------------------------|----------|-----------------------------------------------------------------------------------------------------------------------|
| acc_id                    | Y        | Account ID                                                                                                            |
| month_tag                 | Y        | Month tag of the monthly report                                                                                       |
| tech_adopter              | Y        | Indicates whether the prospect is a technology adopter                                                                |
| wrble_dev                 | Y        | Indicates whether the prospect has a wearable device                                                                  |
| wrble_dev_home_util       | Y        | Indicates whether the prospect uses a wearable device to track home utilities                                         |
| wrble_dev_drv_beh         | Y        | Indicates whether the prospect uses a wearable device to track driving behavior                                       |
| wrble_dev_fina_info       | Y        | Indicates whether the prospect uses a wearable device to track financial information                                  |
| wrble_dev_health          | Y        | Indicates whether the prospect uses a wearable device to track health and fitness activities and info                 |
| wrble_dev_med_cons        | Y        | Indicates whether the prospect uses a wearable device to track media consumption                                      |
| wrble_dev_ret_info        | Y        | Indicates whether the prospect uses a wearable device to track retail information                                     |
| wrble_dev_trav_ent        | Y        | Indicates whether the prospect uses a wearable device to track travel and entertainment activities                    |
| int_shop                  | Y        | Indicates whether the prospect prefers shopping/buying via the internet                                               |
| mail_shop                 | Y        | Indicates whether the prospect prefers shopping/buying via the mail                                                   |
| phone_shop                | Y        | Indicates whether the prospect prefers shopping/buying via the phone                                                  |
| int_air_tick              | Y        | Indicates whether the prospect shopped for airline tickets via the internet in the last 24 months                     |
| int_bank_serv             | Y        | Indicates whether the prospect shopped for banking services via the internet in the last 24 months                    |
| int_books                 | Y        | Indicates whether the prospect shopped for books via the internet in the last 24 months                               |
| int_car_rent              | Y        | Indicates whether the prospect shopped for car/vehicle rental reservations via the internet in the last 24 months     |
| int_drinks                | Y        | Indicates whether the prospect shopped for coffee and tea via the internet in the last 24 months                      |
| int_cosmet                | Y        | Indicates whether the prospect shopped for cosmetics/toiletries via the internet in the last 24 months                |
| int_cc                    | Y        | Indicates whether the prospect shopped for credit cards via the internet in the last 24 months                        |
| int_flowers               | Y        | Indicates whether the prospect shopped for flowers via the internet in the last 24 months                             |
| int_food                  | Y        | Indicates whether the prospect shopped for food/groceries via the internet in the last 24 months                      |
| int_hotel_rent            | Y        | Indicates whether the prospect shopped for hotel reservations via the internet in the last 24 months                  |
| int_oth_fina              | Y        | Indicates whether the prospect shopped for other financial/insurance products by internet in the last 24 months       |
| int_oth_health            | Y        | Indicates whether the prospect shopped for other health/medical supplies by internet in the last 24 months            |
| int_oth_travel            | Y        | Indicates whether the prospect shopped for other travel services via the internet in the last 24 months               |
| int_prescrip_drugs        | Y        | Indicates whether the prospect shopped for prescription drugs via the internet in the last 24 months                  |
| int_sprt_equip            | Y        | Indicates whether the prospect shopped for sports equipment via the internet in the last 24 months                    |
| nt_vitamins               | Y        | Indicates whether the prospect shopped for vitamins via the internet in the last 24 months                            |
| int_wine                  | Y        | Indicates whether the prospect shopped for wines/champagnes by internet in the last 24 months                         |
| business_fan              | Y        | Indicates whether the prospect is a business fan                                                                      |
| hvy_fb_user               | Y        | Indicates whether the prospect is a heavy Facebook user                                                               |
| hby_lin_user              | Y        | Indicates whether the prospect is a heavy LinkedIn user                                                               |
| hvy_tw_user               | Y        | Indicates whether the prospect is a heavy Twitter user                                                                |
| hvy_yt_user               | Y        | Indicates whether the prospect is a heavy YouTube user                                                                |
| mobile_soc_netwker        | Y        | Indicates whether the prospect is a mobile social networker                                                           |
| photo_pster               | Y        | Indicates whether the prospect is a photo poster                                                                      |
| pst_respder               | Y        | Indicates whether the prospect is a post responder                                                                    |
| soc_influencer            | Y        | Indicates whether the prospect is a social influencer                                                                 |
| soc_influenced            | Y        | Indicates whether the prospect is socially influenced                                                                 |
| txt_pster                 | Y        | Indicates whether the prospect is a text poster                                                                       |
| vid_pster                 | Y        | Indicates whether the prospect is a video poster                                                                      |
| num_wk_frstord            | Y        | Number of weeks since the first order in the household                                                                |
| num_wk_frstord_offln      | Y        | Number of weeks since the first offline order in the household                                                        |
| num_wk_frstord_onln       | Y        | Number of weeks since the first online order in the household                                                         |
| num_wk_lstord             | Y        | Number of weeks since the last order in the household                                                                 |
| num_wk_lstord_offln       | Y        | Number of weeks since the last offline order in the household                                                         |
| num_wk_lstord_onln        | Y        | Number of weeks since the last online order in the household                                                          |
| ttl_num_ord_onln          | Y        | Total number of online orders in the last 24 months                                                                   |
| ttl_amt_ord_onln          | Y        | Total amount from online orders in the last 24 months                                                                 |
| ttl_num_ord_offln         | Y        | Total number of offline orders in the last 24 months                                                                  |
| ttl_amt_ord_offln         | Y        | Total amount from offline orders in the last 24 months                                                                |
| cell_phone                | Y        | Indicates whether the prospect uses a cell phone                                                                      |
| day_tv                    | Y        | Indicates whether the prospect watches daytime TV                                                                     |
| read_mags                 | Y        | Indicates whether the prospect reads magazines                                                                        |
| read_news                 | Y        | Indicates whether the prospect reads newspapers                                                                       |
| listen_radio              | Y        | Indicates whether the prospect uses the radio                                                                         |
| mail_prescrip             | Y        | Indicates whether the prospect prescriptions by mail                                                                  |
| mobile_wlet_user          | Y        | Indicates whether the prospect is a mobile wallet power user                                                          |
| fit_brand                 | Y        | Indicates whether the prospect personally own a fitness band                                                          |
| smart_watch               | Y        | Indicates whether the prospect personally own a smartwatch                                                            |
| inter_mobile_wlet_info    | Y        | Indicates whether the prospect is interest in using a mobile wallet for storing general information                   |
| inter_mobile_wlet_paymts  | Y        | Indicates whether the prospect is interest in using a mobile wallet for storing payment options                       |
| inter_mobile_wlet_te      | Y        | Indicates whether the prospect is interest in using a mobile wallet for T&E (ticket storage, food ordering, etc.)     |
| inter_mobile_wlet_discnt  | Y        | Indicates whether the prospect is interest in using a mobile wallet to get store or restaurant discounts or offers    |
| inter_wrble_dev_home_util | Y        | Indicates whether the prospect is interest in using a wearable device to track home utilities                         |
| inter_wrble_dev_drv_beh   | Y        | Indicates whether the prospect is interest in using a wearable device to track driving behavior                       |
| inter_wrble_dev_fina_info | Y        | Indicates whether the prospect is interest in using a wearable device to track financial information                  |
| inter_wrble_dev_health    | Y        | Indicates whether the prospect is interest in using a wearable device to track health and fitness activities and info |
| inter_wrble_dev_med_cons  | Y        | Indicates whether the prospect is interest in using a wearable device to track media consumption                      |
| inter_wrble_dev_ret_info  | Y        | Indicates whether the prospect is interest in using a wearable device to track retail information                     |
| inter_wrble_dev_trav_ent  | Y        | Indicates whether the prospect is interest in using a wearable device to track travel and entertainment activities    |
| app_pay_user              | Y        | Indicates whether the prospect is an Apple Pay power user                                                             |
| goog_pay_user             | Y        | Indicates whether the prospect is a Google Pay power user                                                             |
| paypal_user               | Y        | Indicates whether the prospect is a PayPal power user                                                                 |
----------------------------------------------------------------------------------------------------------------------------------------------------------------

- **_Transaction.csv_** (*OPTIONAL*):

| Column      | Required | Meaning                                   |
|-------------|----------|-------------------------------------------|
| trans_id    | Y        | Unique record ID of transaction           |
| acc_id      | Y        | Account ID associate with the transaction |
| trans_date  | Y        | Datetime of transaction                   |
| trans_amt   | Y        | Amount of transaction                     |
| is_approved | Y        | Whether the transaction is approved       |
| merch_id    | N        | Merchant ID                               |
| mcc_code    | N        | MCC code of merchant's industry           |
----------------------------------------------------------------------


## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.zip.out

| Column     | Meaning                                                   |
|------------|-----------------------------------------------------------|
| acc_id     | Account's unique ID                                       |
| prop_score | Propensity score to respond to direct mail for a prospect |
