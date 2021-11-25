# Input/Output Description

## Input:
The client should provide one comma separated (CSV) file in the below format. Reference file: sample.csv

- **_interest_rate.csv _** (*REQUIRED*):

| Column               | Column Required? | Meaning                                     |
|----------------------|------------------|---------------------------------------------|
| month_tag            | Y                | year month                                  |
| IR                   | Y                | interest rate                               |
	
## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.csv.out
   - month_tag: year month
   - baseline: interest rates for Baseline scenario
   - optimistic: interest rates for Optimistic scenario
   - pessimistic: interest rates for Pessimistic scenario
