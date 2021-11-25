# Input/Output Description

- Input: A zip file containing upto 3 comma separated csv files (2 required). **__Reference file: sample.zip__**
- Details for each csv file:
    - supplier.csv (required)
        - Required columns: 
            - supplier_id: unique supplier identifier
            - sup_creation_date: supplier creation date
            - diversity_ind: indicator whether the supplier is a diverse supplier

    - transaction.csv (required)
        - Required columns: 
            - txn_id: unique transction identifier
            - posting_date: posting date for the transaction
            - amount_usd: invoice spend amount
            - supplier_id: supplier identifier
            - bu_code: business unit code
            - category_name: category name
            - sub_category_name: sub cateory name
            - commodity_name: commodity name
            - sector_name: sector name
            - merchant_code: merchant code

    - sup_preferred_list.csv (optional)
        - Required columns:
            - supplier_id: preferred supplier id
            - sub_category_name: sub cateory name corresponding to the preferred supplier

    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.
    
## Output
- Output: a JSON list of objects containing the predicted rank on supplier_id and sub category level. **__Reference file: sample.zip.out__**
 - Columns:
        - supplier_id: supplier identifier
        - sub_category_name: sub cateory name
        - supplier_rank: predicted rank based on the model score for the suppliler of a sub category
