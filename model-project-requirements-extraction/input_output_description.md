# Input/Output Description

## Input:
A **zip file** with docx files of project document in docx format. Reference file: sample.zip


## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.zip.out

 - FileName: Filename of docx file
 - Domain_Predicted_Labels: the domains involved in the SOWs in contracts, such as 'Anomaly & Fraud Detection' and 'Revenue Leakage Control'. One contract may cover multiple domains.
 - Specialty_Predicted_Labels: the specialties need for taking responsibility of the work stated in contracts, such as 'Project/Program/Account Management' and 'Data Management/ETL Development'. One contract may cover multiple specialties.
 - Modeling: the models or the techniques that would be used when implementing SOWs, such as “NLP” and “LR”.
 - Coding: the coding language that would be used, such as “Java” and “Python”.
