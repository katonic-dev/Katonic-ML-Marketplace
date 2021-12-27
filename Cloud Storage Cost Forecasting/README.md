# Cloud Storage Cost Forecasting
The solution provides 24 hours future forecast of the cost incurred for cloud storage using historical data.

# Product Overview
Cloud storage cost forecasting helps businesses assess the cost incurred from their cloud storage based on historic data. This will help businesses get some understanding of the potential cost for their cloud resources and help them plan better to manage storage services like S3 buckets, EC2 storage, Elastic Block Store, Amazon Glacier etc. It uses an open-source Prophet library which is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

# Highlights
1. This solution will take in hourly cost of cloud compute resources as input and provide 24 hours of future forecast. 

2. Time Series Forecasting can be applied in forecasting cloud storage cost
