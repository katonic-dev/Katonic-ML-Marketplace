# Input/Output Description

## Input:
A **zip file** with the following comma separated csv files. Reference file: sample.zip

- **_scholarship_records.csv_** (*OPTIONAL*): 
    
| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | Unique ID for Individual                                                                               |
| ACADEMIC_YEAR              | Y                | Code for Academic Year of Scholarship                                                                  |
| SCHOLARSHIP_PERIOD         | Y                | Code for Academic Period of Scholarship, eg, 1 for spring only, 2 for fall only, 3 for spring and fall |
| SCHOLARSHIP_CODE           | Y                | Code for Scholarship                                                                                   |

- **_education_history.csv_** (*REQUIRED*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | Unique ID for Individual                                                                               |
| INSTITUTION                | Y                | Institution Name                                                                                       |
| DEGREE_TYPE                | Y                | Degree Type                                                                                            |
| DEGREE YEAR                | Y                | Degree Year                                                                                            |
| DEGREE_MAJOR               | Y                | Degree major                                                                                           |
| INSTITUTION_CITY           | Y                | Institution City                                                                                       |
| INSTITUTION_STATE          | Y                | Institution State                                                                                      |
| INSTITUTION_COUNTRY        | Y                | Institution Country                                                                                    |
| SCIENCE_GPA                | Y                | GPA of all Biology, Chemistry, Physics, and Math courses                                               |
| MATH_GPA                   | N                | GPA of all Math courses                                                                                |
| PHYSICS_GPA                | N                | GPA of all Physics courses                                                                             |
| CHEMISTRY_GPA              | N                | GPA of all Chemistry courses                                                                           |
| BIOLOGY_GPA                | N                | GPA of all Biology courses                                                                             |
| OVERAL_GPA                 | Y                | OVERAL_GPA                                                                                             |


- **_standard_exam_records.csv_** (*REQUIRED*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | ID of individual                                                                                       |
| EXAM_VERSION               | N                | Exam version, if there are different versions                                                          |
| TOTAL_SCORE_RANGES         | Y                | The range of test score                                                                                |
| TEST_DATE                  | Y                | Date of the test/exam                                                                                  |
| PART1_SCORE                | Y                | The score of the forst part of exam, if the test has multiple parts                                    |
| PART2_SCORE                | Y                | Similar to above, can have any number of parts, depending on the exam                                  |
| TOTAL_SCORE                | Y                | Total score                                                                                            |

- **_interview_summary.csv_** (*REQUIRED*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | Unique ID for Individual                                                                               |
| INTERVIEW_DATE             | Y                | Interview Date                                                                                         |
| INTERVIEWER_RECOMMENDATION | Y                | Interviewer Recommendation                                                                             |
| INTERVIEW_TYPE             | Y                | Interview Type                                                                                         |

- **_interview_score.csv_** (*REQUIRED*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | Unique ID for Individual                                                                               |
| INTERVIEW_ITEM             | Y                | Description of the interview item, eg: skills, personality, etc                                        |
| TEST_SCORE                 | Y                | Test Score                                                                                             |
| TEST_DATE                  | Y                | Test Date                                                                                              |

- **_profile.csv_** (*OPTIONAL*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | ID of individual                                                                                       |
| CITIZENSHIP_IND            | Y                | Y or N if CITIZEN or US Permanent Resident                                                             |
| NATIONALITY                | Y                | Citizenship Country                                                                                    |
| GENDER                     | Y                | Male or female                                                                                         |
| ADMISSIONS_TYPE            | Y                | admission type, eg: 'R' for re-addmission, 'N' for new addmission                                      |
| ADMIT_MONTH                | Y                | Admit Month                                                                                            |
| ADMIT_YEAR                 | Y                | Admit Year                                                                                             |
| FAMILY_ALUMNI_IND          | Y                | Yes if family members attend the univeristy before                                                     |
| MARITAL_STATUS_DESC        | Y                | Marital status                                                                                         |
| NATION_OF_BIRTH_DESC       | Y                | Nation of Birth                                                                                        |
| NATIVE_LANGUAGE_DESC       | Y                | Native language                                                                                        |

- **_application_essay.csv_** (*OPTIONAL*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | ID of individual                                                                                       |
| APPLICATION_TERM           | Y                | Term for application                                                                                   |
| QUESTION                   | Y                | Question                                                                                               |
| SHORT_ANSWER               | Y                | Short Answer                                                                                           |
| LONG_ANSWER                | Y                | Long Answer                                                                                            |

- **_address.csv_** (*OPTIONAL*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | ID of individual                                                                                       |
| CITY                       | Y                | City                                                                                                   |
| STATE                      | Y                | State or Province                                                                                      |
| POSTAL_CODE                | Y                | Postal Code                                                                                            |
| NATION_DESC                | Y                | Nation                                                                                                 |

- **_survey.csv_** (*OPTIONAL*): 

| Column                     | Column Required? | Meaning                                                                                                |
|----------------------------|------------------|--------------------------------------------------------------------------------------------------------|
| ID                         | Y                | ID of individual                                                                                       |
| SURVEY_DATE                | Y                | Survey date                                                                                            |
| Question1                  | Y                | Anwser of Survey Question1                                                                             |
| Question2                  | Y                | Answer of Survey Question2                                                                             |
| Question3                  | Y                | Anwser of Survey Question2                                                                             |
| Question4                  | Y                | Answer of Survey Question3                                                                             |
| Question5                  | Y                | Anwser of Survey Question3                                                                             |
| Question6                  | Y                | Answer of Survey Question4                                                                             |
| Question7                  | Y                | Anwser of Survey Question4                                                                             |
| Question8                  | Y                | Answer of Survey Question5                                                                             |
| Question9                  | Y                | Anwser of Survey Question2                                                                             |
| Question10                 | Y                | Answer of Survey Question3                                                                             |


## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.zip.out

| Column | Column Required? | Meaning                                                                  |
|--------|------------------|--------------------------------------------------------------------------|
| ID     | Y                | ID of individual                                                         |
| SCORE  | Y                | Propensity score indicate that the student's likelihood to fail the exam      |
