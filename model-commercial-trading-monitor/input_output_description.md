# Input/Output Description

- Input: The client should provide the following formatted data in CSV files (3 required, 2 optional). Below are the details for each CSV file. Reference file: sample.zip

| Raw Table             | Table Required? | Column                         | Column Required? | Meaning                                                                          |
|-----------------------|-----------------|--------------------------------|------------------|----------------------------------------------------------------------------------|
| route_info.csv        | Y               | ROUTE_ID                       | Y                | Unique identifier for each route                                                 |
|                       |                 | ORIGIN                         | Y                | source of the journey                                                            |
|                       |                 | DESTINATION                    | Y                | destination of journey                                                            |
|                       |                 | CAPACITY                       | Y                | Capacity of no of passengers                                                     |
|                       |                 | IS_DIRECT_FLIGHT               | Y                | if this is the direct flight, Yes & No                                       |
|                       |                 | WEEKLY_FREQUENCY               | Y                | How many flights are there in per week                                           |
| booking_info.csv      | Y               | BOOKING_ID                     | Y                | order id                                                                         |
|                       |                 | CUSTOMER_ID                    | Y                | customer id                                                                      |
|                       |                 | DATE_OF_BOOKING                | Y                | date on which booking was made                                                   |
|                       |                 | FIGHT_CODE                     | Y                | flight number                                                                    |
|                       |                 | PAYMENT_AMT                    | Y                | Amount of booking                                                                |
|                       |                 | SCHEDULED_DEPART_TIME          | Y                | departure time                                                                   |
|                       |                 | SCHEDULED_ARRIVAL_TIME         | Y                | arrival time                                                                     |
|                       |                 | DEPART_AIRPORT                 | Y                | source of the journey                                                            |
|                       |                 | ARRIVAL_AIRPORT                | Y                | destination of journey                                                             |
|                       |                 | COUPON_IND                     | Y                | Coupon id if used                                                                |
|                       |                 | LEISURE_IND                    | Y                | Indicates whether this booking flight item record is a leisure round trip         |
|                       |                 | REDEMPTION_IND                 | Y                | Indicates whether this Booking Flight Item record is a redemption booking        |
|                       |                 | NUM_SEGMENTS                   | Y                | Number of segments of the flight                                                 |
| Sales_target_info.csv | Y               | ROUTE_ID                       | Y                | Unique identifier for each route                                                 |
|                       |                 | FARE                           | Y                | fare for 1 journey of source to destination for one passenger                     |
|                       |                 | WEEK                           | Y                | week for which target was given                                                  |
|                       |                 | TARGET_VOLUME                  | Y                | target volume of sales                                                           |
|                       |                 | SALES_VOLUME                   | Y                | actual sales volume achieved                                                     |
|                       |                 | DISCOUNT_OFFERED               | Y                | if there is any discount offered by the carrier                                  |
|                       |                 | IS_HOLIDAY_SEASON              | N                | if the target is set for a holiday or festive season yes/no                      |
| web_traffic_info.csv  | N               | SESSION_ID                     | Y                | unique identifier for each visitor                                              |
|                       |                 | BACK_LINKS                     | Y                | is the customer visiting the website by clicking on any advertisement link YES/NO |
|                       |                 | IS_CONVERTED                   | Y                | if the customer makes a purchase YES/NO                                          |
|                       |                 | IS_NEW_CUSTOMER                | Y                | is the customer making a booking first time YES/NO                               |
|                       |                 | NO_TIMES_VISITED               | Y                | No of times user visit the website before making the booking                     |
|                       |                 | IS_PRICE_SENSITIVE             | N                | is the customer price sensitive YES/NO                                           |
| marketing_info.csv    | N               | ROUTE_ID                       | Y                | Unique identifier for each route                                                 |
|                       |                 | COMPETITIVE_STRENGTH           | Y                | Does the carrier has competitive business in this route YES/NO                   |
|                       |                 | NO_OF_COMPETITORS              | N                | No of competitor in this route                                                   |
|                       |                 | Tier Strength                  | N                | strength of user in this route (scale of 1 to 5 , 5 is highest)                  |
|                       |                 | DISCOUNT_OFFERED_BY_COMPETITOR | N                | is customer offering any discount on this route (YES/NO)                         |
|                       |                 | COMPETITOR AVERAGE FARE        | N                | Average fare of the competitor in this route                                    |
|                       |                 | FARE                           | Y                | Fare of the carrier on this route                                                |
    

- Output: a JSON list of objects contaning, for each record in the original orderthe following fields:
    | Column       | Column Required? | Meaning                                                                                                                                                                                |
    |--------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Route_id     | Y                | Unique Identifier for each route for which the sales have to be predicted
    | Week         | Y                | week for which the sales have to be predicted (value is in range of 1 to 52 : 1 is 1st week of year and 52 is last week of year)                                                                                                                                                                            |
    | Volume       | Y                | Predicted sales volume for given route and week  
 -Reference file: sample.zip.out
