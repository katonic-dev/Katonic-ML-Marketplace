# Input/Output Description

## Input:
A **zip file** with resumes in docx format. Reference file: sample.zip


## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.zip.out

- FileName: filename of resume (docx file).
- Domain_Predicted_Labels: the domains involved in their resume, such as 'Anomaly & Fraud Detection' and 'Risk Management'.
  One resume may cover multiple domains.
- Specialty_Predicted_Labels: the specialties need for taking responsibility of the work stated in their resumes, 
  such as 'Database Architecture and Management' and 'Product Management'. 
- Coding: the coding languages that were stated in their resume, such as “Java” and “Python”.
- Modeling: the models or the techniques that were stated in their resume, such as “NLP” and “LR”.
