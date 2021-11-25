# Input/Output Description

- Input: A zip file with the following comma separated csv files (3 Required 1 optional). Reference file: sample.zip. 

- **_passenger_info.csv_** (*REQUIRED*): 
    
| Column          | Column Required? | Meaning                                     |
|-----------------|------------------|---------------------------------------------|
| PASSENGER_ID    | Y                | Customer Identifier                         |
| MEMBERSHIP_ID   | Y                | Memship ID if the customer has a membership |
| BIRTH_DAY       | Y                | Birthday of Customer                        |
| NET_WORTH       | Y                | The customer's networth                     |
| GENDER          | Y                | Gender of customer                          |
| ADDRESS_COUNTRY | Y                | Country of customer's address               |
| ADDRESS_STATE   | Y                | State of customer's address                 |
| ADDRESS_CITY    | Y                | City of customer's address                  |
| ADDRESS_ZIPCODE | Y                | Zipcode of customer's address               |    

- **_flight_booking_history.csv_** (*REQUIRED*): 

| Column          | Column Required? | Meaning                                     |
|-----------------|------------------|---------------------------------------------|
| PASSENGER_ID    | Y                | Customer Identifier                         |
| MEMBERSHIP_ID   | Y                | Memship ID if the customer has a membership |
| BIRTH_DAY       | Y                | Birthday of Customer                        |
| NET_WORTH       | Y                | The customer's networth                     |
| GENDER          | Y                | Gender of customer                          |
| ADDRESS_COUNTRY | Y                | Country of customer's address               |
| ADDRESS_STATE   | Y                | State of customer's address                 |
| ADDRESS_CITY    | Y                | City of customer's address                  |
| ADDRESS_ZIPCODE | Y                | Zipcode of customer's address               |

- **_upgrade_history.csv_** (*REQUIRED*): 
    
| BOOKING_ID    | Y | BOOKING ID associate with the upgrade                           |
|---------------|---|-----------------------------------------------------------------|
| PASSENGER_ID  | Y | Customer id of customer who place the order                     |
| FIGHT_CODE    | Y | Flight Code                                                     |
| INTIAL_CABIN  | Y | original Cabin                                                  |
| UPGRADE_CABIN | Y | cabin after upgrading                                           |
| AIRPORT       | Y | airport where the upgrade was made if it is upgraded at airport |
| DATE          | Y | Date of the upgrade                                             |
| DISCOUNT_IND  | Y | Whether the upgrade is a discount upgrade                       |

- **_transaction_history.csv_** (*OPTIONAL*): 
    
| Column       | Column Required? | Meaning                                                    |
|--------------|------------------|------------------------------------------------------------|
| PASSENGER_ID | Y                | Passenger ID                                               |
| DATE         | Y                | Date of the transaction                                    |
| ITEM         | Y                | The code for items, such as meal, entertainment, gift, etc |
| AMOUNT       | Y                | The paid amount for the item                               |

    

- Output: a JSON list of objects contaning, for each record in the original orderthe following fields:
    - PASSENGER_ID: Passenger ID
    - SCORE:  Propensity Scofe indicating the likelihood that the customer will take advantage of discounted upgrades to travel in premium cabins rather than purchasing premium cabins at full fare.  
- Reference file: sample.zip.out
