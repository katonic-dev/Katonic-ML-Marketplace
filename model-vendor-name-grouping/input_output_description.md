# Input/Output Description

## Input:
The client should provide one comma separated (CSV) file in the below format. Reference file: sample.csv 

- **_vendor_list.csv_** (*REQUIRED*): 
    
| Column               | Column Required? | Meaning                                     |
|----------------------|------------------|---------------------------------------------|
| Vendor_Name_raw      | Y                | Unique vendors' name                        |
| Spend_Amount         | N                | clients' expense on these vendors           |

	
## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.csv.out
   - Vendor_Name_raw: (input) unique vendors' name
   - Spend_Amount: clients' expense on this vendor 
   - Vendor_Group_Name: (final output) group name which this vendor belongs to 
	
	
