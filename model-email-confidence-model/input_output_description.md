# Input/Output Description

- Input: Data at the customer level (each bullet point is a field); all IDs must be present. Below are the details for the input CSV file. 

    - **_Email_Info.csv_** (*REQUIRED*): 

    | Column              | Required | Meaning                                                              |
    |---------------------|----------|----------------------------------------------------------------------|
    | email_addr_id       |     Y    | Unique ID associated with the email address                          |
    | email_addr          |     Y    | Email address                                                        |
    | business_name       |     Y    | Name of business trying to reach                                     |
    | ao_first_name_one   |     Y    | 1st authorized officer’s first name                                  |
    | ao_last_name_one    |     Y    | 1st authorized officer’s last name                                   |
    | ao_first_name_two   |     N    | 2nd authorized officer’s first name (enter "N/A" if no 2nd officer)  |
    | ao_last_name_two    |     N    | 2nd authorized officer’s last name (enter "N/A" if no 2nd officer)   |
    | ao_first_name_three |     N    | 3rd authorized officer’s first name (enter "N/A" if no 3rd officer)  |
    | ao_last_name_three  |     N    | 3rd authorized officer’s last name (enter "N/A" if no 3rd officer)   |
    | ao_first_name_four  |     N    | 4th authorized officer’s first name (enter "N/A" if no 4th officer)  |
    | ao_last_name_four   |     N    | 4th authorized officer’s last name (enter "N/A" if no 4th officer)   |
    | ao_first_name_five  |     N    | 5th authorized officer’s first name (enter "N/A" if no 5th officer)  |
    | ao_last_name_five   |     N    | 5th authorized officer’s last name (enter "N/A" if no 5th officer)   |
    
**__Reference file: sample.csv__**
    
## Output
- Output: a JSON list of objects with the email address ID as the main key; for every email address ID, there is a corresponding email address and business name along with the **_associated score_**. The associated score is the probability that a certain email address is associated with the given corresponding business name. 

| Column        | Meaning                                                                        |
|---------------|--------------------------------------------------------------------------------|
| email_addr_id | Unique ID associated with the email address                                    |
| email_addr    | Email address                                                                  |
| business_name | Name of business trying to reach                                               |
| assoc_score   | Probability that an email address is correctly associated with a business name |--------------------------------------------------------------------------------------------------

**__Reference file: sample.csv.out__**
