# Input/Output Description
- Input: 4 comma separated csv
- Details for each csv file:
    - account_profile.csv (required)
        - Required columns: 
            - acc_id: account identifier 
            - age: age
            - acc_type: account type, like Business, Government, Individual,…
            - gender: account gender
            - Latitude: Latitude of the billing address
            - Longitude: Longitude of the billing address
            - tenure: account tenure, months

    - data_usage.csv (required)
        - Required columns: 
            - record_id: uniqe id of each service1 usage record
            - acc_id: account identifier 
            - record_time: date of the service usage record of the account
            - 2G_usage: amount of 2G data usage
            - 3G/4G_usage: amount of 3G/4G data usage
            - LTE_usage: amount of LTE data usage

    - device.csv (required)
        - Required columns: 
            - acc_id: account identifier 
            - device_id: device identifier 
            - upgrade_ind: indicator whether the acc has upgraded the device or not
            - activiation_date: device activiation date
            - eip_ind: indicator that the device is on an equipment installment plan
            - smart_ind: indictor that device is a smartphone
            - sim_device_ind: indictor of device using SIM card
            - manufacturer_group: type of main stream manufacturer,like Samsung, Apple,...

    - survey.csv (required)
        - Required columns: 
            - acc_id: account identifier 
            - survey_start_date: date when survey started
            - response_date: date when the survey get a response
            - likelihood_to_recommend: likelihood to give a recommendation
            - overall_satisfaction: overall satisfication score
            - likelihood_to_continue: likelihood to contiue using it
            - overall_coverage_reception: overall coverage reception
            - coverage_reception_at_your_home: coverage reception at home
            - coverage_reception_away_from_your_home: coverage reception away from home
            - data_speeds: average data speed
            - monthly_plan_price: monthly plan price for the service
        - Optional columns:
            - ind_badNet: target variable, 1 means bad network experience

    - Note: if end user do not have optional tables, empty CSV with identical columns should be generated to replace missing optional table.
	
- Output: a JSON list of objects contaning, for each record in the original orderthe following fields:
    - acc_id: account identifier
    - nex_score:  predicted network experience score from 1 to 10, higher value means better network experience.
 - Reference file: sample.zip.out	
	
