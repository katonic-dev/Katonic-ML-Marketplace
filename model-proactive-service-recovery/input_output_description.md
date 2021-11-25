# Input/Output Description

- Input: A zip file containing 4 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - **_customer.csv_** (*REQUIRED*): customer information
    
    | Column          | Column Required? | Meaning                                     |
    |-----------------|------------------|---------------------------------------------|
    | CUSTOMER_ID     | Y                | Customer Identifier                         |
    | MEMBERSHIP_ID   | Y                | Memship ID if the customer has a membership |
    | BIRTH_DAY       | Y                | Birthday of Customer                        |
    | NET_WORTH       | Y                | The customer's networth                     |
    | GENDER          | Y                | Gender of customer                          |
    | ADDRESS_COUNTRY | Y                | Country of customer's address               |
    | ADDRESS_STATE   | Y                | State of customer's address                 |
    | ADDRESS_CITY    | Y                | City of customer's address                  |
    | ADDRESS_ZIPCODE | Y                | Zipcode of customer's address               |
    

    - **_order.csv_** (*REQUIRED*): historical order records, order can be booking, purchasing, etc
    
    | Column          | Column Required? | Meaning                                                                          |
    |-----------------|------------------|----------------------------------------------------------------------------------|
    | ORDER_ID        | Y                | Order ID                                                                         |
    | CUSTOMER_ID     | Y                | Customer id of customer who place the order                                      |
    | ORDER_TIME      | Y                | The datetime when the order is placed                                            |
    | ORDER_AMT       | Y                | The amount of the order                                                          |
    | SERVICE_CODE    | Y                | The service code involve in the order, each code represent a unique service type |
    | SERVICE_TIME    | Y                | The datetime that the service is scheduled                                       |
    
    
    - **_event.csv_** (*REQUIRED*): historical records of event which affect services and cause complaints 
    
    | Column                 | Column Required? | Meaning                                                                          |
    |------------------------|------------------|----------------------------------------------------------------------------------|
    | EVENT_ID               | Y                | The ID of event                                                                  |
    | EVENT_STARTTIME        | Y                | The start time of the event                                                      |
    | EVENT_ENDTIME          | Y                | The end time of the event                                                        |
    | EVENT_CODE             | Y                | The code of event, each code represent an unique type of event                   |
    | EVENT_DESC             | N                | The description of the event                                                     |
    | SERVICE_CODES_INVOLVED | Y                | The service codes of services involved in the event, seperated by comma          |
    
    
    - **_complaints.csv_** (*REQUIRED*): historical records of complaints cases. 
    
    | Column                 | Column Required? | Meaning                                                                          |
    |------------------------|------------------|----------------------------------------------------------------------------------|
    | CASE_ID                | Y                | The customer complain case ID                                                    |
    | ORDER_ID               | Y                | The order number get involved in the case                                        |
    | CUSTOMER_ID            | Y                | The customer who open the case                                                   |
    | EVENT_CODE             | Y                | The event code associated with the complain                                      |
    | SERVICE_CODE           | Y                | The service involved in the case                                                 |
    | CASE_OPEN_TIME         | Y                | The time when the case is opened                                                 |
    | CASE_CLOSE_TIME        | Y                | The time when the case is closed                                                 |
    | RESOLVED_IND           | Y                | Indicator of whether the case is resolved                                        |
    | SATISFACTORY_SCORE     | Y                | The satifactory score given by the customer after the case is closed             |
            
## Output
- Output: a JSON list of objects containing CUSTOMER_ID: customer ID of customers and SCORE: propensity score that a customer will complain about a failure. **__Reference file: sample.zip.out__**

