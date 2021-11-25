# Input/Output Description

## Input:
The client should provide one comma separated (CSV) file in the below format. Reference file: sample.csv 

 - **_transaction_info.csv_** (*REQUIRED*): 
    
| Column                 | Column Required?  | Meaning                                                     |
|------------------------|-------------------|-------------------------------------------------------------|
| TRANSACTION_ID         | Y                 | Unique transaction ID of the transaction                    |
| SUPPLIER_PARENT_NAME   | Y                 | Supplier name in the invoice of transaction                 |
| SUPPERLIER_NAME        | Y                 | The parent company of the supplier                          |
| MATERIAL_DESCRIPTION   | Y                 | The material/porduct involved in the invoice                |
| GL_ACCOUNT_DESCRIPTION | Y                 | The description of related financial report category        |
| INVOICE_DESCRIPTION    | Y                 | The description in the invoice                              |
| MCC_DESCRIPTION        | Y                 | The description of the supplier's merchandise category code |
| PO_DESCRIPTION         | Y                 | The description of the purchase order                       |
| AMOUNT                 | Y                 | The amount involved in the invoice                          |
 
	
## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.csv.out
| Column         | Column Required? | Meaning                                  |
|----------------|------------------|------------------------------------------|
| TRANSACTION_ID | Y                | Unique transaction ID of the transaction |
| PREDICTION     | Y                | Prediction of the transaction type       |                                                               
	 

	
