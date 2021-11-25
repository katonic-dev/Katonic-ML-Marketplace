# Input/Output Description

- Input: A zip file containing 2 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - **_creditcard_pnl.csv_** (*REQUIRED*): 
    
    | Column                    | Column Required? | Meaning                                                   |
    | ------------------------- | ---------------- | --------------------------------------------------------- |
    | month                     | Y                | month tag of the monthly report                           |
    | accountID                 | Y                | accountID                                                 |
    | credit\_line              | Y                | credit line at PNL date                                   |
    | tenure                    | Y                | tenure                                                    |
    | 3rd\_party\_credit\_score | Y                | 3rd part score. Eg: FICO                                  |
    | balance\_transfer\_cnt    | Y                | number of balance transfer records occurred in this month |
    | balance\_transfer\_amt    | Y                | amount of balance transfer records occurred in this month |
    | gross\_payment\_cnt       | Y                | number of total payment records occurred in this month    |
    | gross\_payment\_amt       | Y                | amount of total payment transfer  occurred in this month  |
    | payment\_reversal\_cnt    | Y                | number of payment reversal records occurred in this month |
    | payment\_reversal\_amt    | Y                | amount of payment reversal occurred in this month         |
    | net\_payment\_amt         | Y                | amount of net payment occurred in this month              |
    | late\_payment\_cnt        | Y                | number of late payment occurred in this month             |
    | auto\_payment\_cnt        | Y                | number of auto payment occurred in this month             |
    | auto\_pay\_enrolled       | Y                | whether enrolled in autopay                               |
    | spend\_amt                | Y                | total spend amount of the account                         |
    | cur\_apr                  | Y                | current APR of the account                                |
    | cash\_advance\_amt        | Y                | cash\_advance in PNL                                      |
    | balance\_amt              | Y                | current balance                                           |
    

    - **_bureau_info.csv_** (*REQUIRED*): 
    
    | Column                   | Column Required? | Meaning                                     |
    | ------------------------ | ---------------- | ------------------------------------------- | 
    | month                    | Y                | month tag of the monthly report             | 
    | accountID                | Y                | accountID                                   | 
    | total\_NC\_balance\_amt  | Y                | total balance amout of all NC trade account |
    | total\_NC\_credit\_limit | Y                | total credit limit of all NC trade account  | 
    | bureau\_utilization      | Y                | utilization ratio of total credit limit     | 
    | risk\_score              | Y                | risk score of the account                   |


## Output
- Output: a JSON list of objects containing accountID (accountID of accounts shown in input files) and APR (model's prediction of the accounts' suggested APR rates). **__Reference file: sample.zip.out__**
