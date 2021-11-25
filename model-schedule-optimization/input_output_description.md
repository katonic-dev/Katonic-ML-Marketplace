# Input/Output Description

- Input: A zip file containing 6 comma separated (csv) files. **__Reference file: sample.zip__**
- Details for each csv file:
    - **_Transaction.csv_** (*REQUIRED*): 

    | Column           | Required | Meaning                                |
    |------------------|----------|----------------------------------------|
    | site_id          |    Y     | Unique cinema location ID              |
    | trans_date       |    Y     | Date of transactions                   |
    | tot_ticket_sales |    Y     | Total daily ticket sales               |
    | tot_trans_amt    |    Y     | Total daily sales                      |
    | trans_fee        |    Y     | Transaction fee for site (the percent) |
    | tax_rate         |    Y     | Tax rate on sales for site             |
    | book_type        |    Y     | Booking type                           |
    | book_fee         |    Y     | Booking fee for tickets (the percent)  |
    | site_book_fee    |    Y     | Booking fee for site (the percent)     |
    ------------------------------------------------------------------------

    - **_Parameter.csv_** (*REQUIRED*): 

    | Column                 | Required | Meaning                                                                                                              |
    |----------------------- |----------|----------------------------------------------------------------------------------------------------------------------|
    | site_id                |     Y    | Unique cinema location ID                                                                                            |
    | targ_week_days         |     Y    | Specifies all days within the target week which defaults to 7 days of the target week                                |
    | tw_earliest_start_date |     Y    | Specifies the earliest date at which the run should begin (i.e. earliest date before start of the target week)       |
    | tw_end_date            |     Y    | Cut-Off date on which the schedule run is carried out                                                                |
    | tw_start_time          |     Y    | Specifies the time of the start day for the run                                                                      |
    | tw_end_time            |     Y    | Specifies the time at the end of the cut-off day for the run (must be in HH:MM format)                               |
    | min_shows              |     Y    | Minimum number of screen showings per day (must be in HH:MM format.)                                                 |
    | max_shows              |     Y    | Maximum number of screen showings per day                                                                            |
    | movie_special          |     Y    | Any movie specials (i.e "N" or "Y")                                                                                  |
    | ticket_price_adj       |     Y    | Adjust the ticket price of a film for this run (i.e. +/- 0.50 cents)                                                 |
    | earliest_open_time     |     Y    | Earliest time at which the cinema opens (must be in HH:MM format)                                                    |
    | latest_close_time      |     Y    | Latest time at which the cinema closes (must be in HH:MM format)                                                     |
    | adult_movie            |     Y    | Over 18s policy meaning no ticket sales for child, family and teens after a specified time (must be in HH:MM format) |
    | seat_override          |     Y    | Overrides for seat capacity at site screen level (value must be a non-negative integer)                              |
    ------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    - **_Movie.csv_** (*REQUIRED*):

    | Column         | Required  | Meaning                                                                                                                    |
    |----------------|-----------|----------------------------------------------------------------------------------------------------------------------------|
    | site_id        |     Y     | Unique cinema location ID                                                                                                  |
    | movie_id       |     Y     | Unique movie ID being shown                                                                                                |
    | movie_type     |     Y     | Type of movies (i.e. preview movies, new movies, holdover movies)                                                          |
    | ticket_type    |     Y     | Type of ticket (i.e. Adult, Adult 3D, Kids AM Adult, Student, Child, Family, and Senior)                                   |
    | ticket_price   |     Y     | Ticket price for movie                                                                                                     |
    | ticket_tax     |     Y     | Tax on ticket price                                                                                                        |
    | pre_bookings   |     Y     | Number of pre-booked tickets pertaining to movie                                                                           |
    | movie_site     |     Y     | Site at which the movie was played                                                                                         |
    | movie_rel_date |     Y     | Movie release date                                                                                                         |
    | movie_name     |     Y     | Name of movie                                                                                                              |
    | movie_status   |     Y     | One of the three values: "Will Not Play", "Specials Only" or "Will Be Considered"                                          |
    | movie_dim      |     Y     | Movie dimension (i.e. 2D or 3D)                                                                                            |
    | movie_genre    |     Y     | Genre of movie (i.e horror, comedy, action, etc.)                                                                          |
    | movie_dura     |     Y     | Length of movie (in minutes)                                                                                               |
    | movie_suit     |     Y     | 1 = system to play movie on this screen type is possible; 0 = movie is not desired to be played on that screen type        |
    | scene_suit     |     Y     | 1 = movie can be scheduled on a scene screen; 0 = movie cannot be scheduled on a scene screen                              |
    | xtreme_suit    |     Y     | 1 = movie can be scheduled on an Xtreme screen; 0 = movie cannot be scheduled on an Xtreme screen                          |
    | gold_suit      |     Y     | 1 = movie can be scheduled on a Gold screen; 0 = movie cannot be scheduled on a Gold screen                                |
    | imax_suit      |     Y     | 1 = movie can be scheduled on an IMAX screen; 0 = movie cannot be scheduled on an IMAX screen                              |
    | other_suit     |     Y     | 1 = movie will play and does not have any screen style for which movie has suitability value as 0; 0 = movie will not play |
    | comp_titles    |     Y     | Comparator titles                                                                                                          |
    | gbor           |     Y     | 1 = new movie will play on site and Opening weekend GBOR is split onto that site; 0 = new movie will not play on site      |
    | distributor    |     Y     | Movie distributor                                                                                                          |
    -----------------------------------------------------------------------------------------------------------------------------------------------------------

    - **_Cinema.csv_** (*REQUIRED*):

    | Column          | Required | Meaning                                                                                                      |
    |-----------------|----------|--------------------------------------------------------------------------------------------------------------|
    | site_id         | Y        | Unique cinema location ID                                                                                    |
    | site_cost       | Y        | Annual cinema location cost                                                                                  |
    | open_util_cost  | Y        | Annual cost for electricity and gas usage when site is open                                                  |
    | close_util_cost | Y        | Annual cost for electricity and gas usage when site is closed                                                |
    | bulb_cost       | Y        | Annual cost for 2D/3D bulbs for site                                                                         |
    | glasses_cost    | Y        | Annual cost for 3D glasses for site                                                                          |
    | staff_hr_cost   | Y        | Total hourly staff costs                                                                                     |
    | min_staff       | Y        | Minimum number of staff employees required                                                                   |
    | seat_cnt        | Y        | Average seat count per screen                                                                                |
    | daily_attend    | Y        | Daily attendance                                                                                            |
    | tot_housenut    | Y        | Total house nut applicable per site (i.e. annual operating expenses cost)                                    |
    | seat_housenut   | Y        | House nut applicable per seat (i.e. sum total of operating expenses for a given time period/number of seats) |
    ---------------------------------------------------------------------------------------------------------------------------------------------

    - **_Schedule.csv_** (*REQUIRED*):

    | Column        | Required | Meaning                                                         |
    |---------------|----------|-----------------------------------------------------------------|
    | movie_id      | Y        | Unique movie ID                                                 |
    | session_id    | Y        | Unique movie session ID                                         |
    | movie_name    | Y        | Name of movie                                                   |
    | movie_date    | Y        | Date of movie screening (shows can be open/cancelled/scheduled) |
    | movie_time    | Y        | Time at which the movie was played (must be in HH:MM format)    |
    | cleaning_time | Y        | Cleaning time between two sessions (must be in HH:MM format)    |
    ----------------------------------------------------------------------------------------------

    - **_Holiday.csv_** (*REQUIRED*):

    | Column         | Required  | Meaning                                                                                                                   |
    |----------------|-----------|---------------------------------------------------------------------------------------------------------------------------|
    | site_id        |     Y     | Unique cinema location ID                                                                                                 |
    | month_date     |     Y     | Holiday data is displayed for one month at a time (everyday date in the month, including the target week)                 |
    | area_holiday   |     Y     | Date is an area specific holiday for site; 1 indicates that the day is a holiday and 0 indicates that it is not a holiday |
    | school_holiday |     Y     | Date is a school holiday for site; 1 indicates that the day is a holiday and 0 indicates that it is not a holiday         |
    | bank_holiday   |     Y     | Date is a bank holiday for site; 1 indicates that the day is a holiday and 0 indicates that it is not a holiday           |
    | other_holiday  |     Y     | Date is another holiday for site; 1 indicates that the day is a holiday and 0 indicates that it is not a holiday          |
    
## Output
- Output: a JSON list of objects containing 'individual optimized schedules for each cinema site with following fields **__Reference file: sample.zip.out__**


| Column            | Meaning                                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------------------------------|
| site_id           | Unique cinema location ID                                                                                          |
| movie_id          | Unique movie ID                                                                                                    |
| session_id        | Unique movie session ID                                                                                            |
| targ_date         | Date in target week (each day during the target week will get its own optimized schedule for each site)            |
| movie_name        | Name of movie                                                                                                      |
| opt_movie_time    | Optimized time at which the movie should be played                                                                 |
| opt_cleaning_time | Optimized cleaning time between two sessions                                                                       |------------------------------------------------------------------------------------------------------------------------------------------

