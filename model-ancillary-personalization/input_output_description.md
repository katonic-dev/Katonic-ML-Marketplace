# Input/Output Description

- Input: A zip file containing 2 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
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

    - **_flight_booking.csv_** (*REQUIRED*): 
    
    | Column                 | Column Required? | Meaning                                                                     |
    |------------------------|------------------|-----------------------------------------------------------------------------|
    | BOOKING_ID             | Y                | Order ID                                                                    |
    | PASSENGER_ID           | Y                | Customer id of customer who place the order                                 |
    | FIGHT_CODE             | Y                | Flight Code                                                                 |
    | BOOKING_TIME           | Y                | The datetime when the order is placed                                       |
    | PAYMENT_AMT            | Y                | The amount of the order                                                     |
    | CABIN                  | Y                | Cabin of the flight, 'F' for first class, 'B' for business, 'E' for economy |
    | SCHEDULED_DEPART_TIME  | Y                | The departure time of the flight                                            |
    | SCHEDULED_ARRIVAL_TIME | Y                | The arrival time of the flight                                              |
    | DEPART_AIRPORT         | Y                | The departure airport 3-digit code                                          |
    | ARRIVAL_AIRPORT        | Y                | The arrival aiport 3-dgit code                                              |
    
    - **_hotel_booking.csv_** (*REQUIRED*): 
    
    | Column            | Column Required? | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    |-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | HOTEL_BOOKING_ID  | Y                | ID number that uniquely identifies the booking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | FLIGHT_BOOKING_ID | Y                | The booking ID of flight that is booked with the hotel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | HOTEL_CODE        | Y                | Unique hotel code (Supplier Code).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | ROOM_TYPE         | Y                | Description of room booked (Shorthand).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | RATE_PLAN_TYPE    | Y                | Pricing codes to determine rates, whether it be standard rates or reduced rates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | MEAL_PLAN_CODE    | Y                | Meal plan code. RO — No food; BB — Breakfast only; HB — Half board (bed, breakfast, evening meal – no drinks included in the evening); FB — Full board (bed, breakfast, lunch, evening meal – no drinks included in the evening); AI — All-inclusive (bed, breakfast, lunch, evening meal, local drinks); UAI — Enhanced all-inclusive (bed, breakfast, lunch, evening meal, all types of drink; HB+ — Bed, breakfast, evening meal + some alcoholic/non-alcoholic drinks; FB+ — Bed, breakfast, lunch, evening meal + some alcoholic/non-alcoholic drinks |
    | PROMO_CODE        | Y                | Promotion / Special offer code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | CHECKIN_DATE      | Y                | Hotel check in date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | CHECKOUT_DATE     | Y                | Hotel check out date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
        
    - **_vehicle_booking.csv_** (*REQUIRED*): 
    
    | Column             | Column Required? | Meaning                                                  |
    |--------------------|------------------|----------------------------------------------------------|
    | VEHICLE_BOOKING_ID | Y                | ID number that uniquely identifies the booking           |
    | FLIGHT_BOOKING_ID  | Y                | The booking ID of flight that is booked with the hotel   |
    | VEHICLE_TYPE_CODE  | Y                | Code Identifies the car type and features                |
    | PICKUP_TIME        | Y                | The date and time the passenger can collect their car    |
    | PICKUP_LOC_CODE    | Y                | The location where the passenger will collect their car  |
    | RETURN_TIME        | Y                | The date and time the passenger should return their car. |
    | RETURN_LOC_CODE    | Y                | The location where the passenger will return their car   |

## Output
- Output: a JSON list of objects containing following fields:
   
   | Field                      | Meaning                                                |
   |-----------------------------|--------------------------------------------------------|
   | PASSENGER_ID                | PASSENGER_ID                                           |
   | FLIGHT_CODE                 | Flight Code                                            |
   | RECOMMEND_HOTEL_CODE        | Recommended hotel code for passenger                   |
   | RECOMMEND_ROOM_TYPE         | Recommended room type for passenger                    |
   | RECOMMEND_PICKUP_LOC_CODE   | Recommended vehicle pickup location code for passenger |
   | RECOMMEND_VEHICLE_TYPE_CODE | Recommended vehicle type code for passenger            |

**__Reference file: sample.zip.out__**
