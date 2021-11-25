# Input/Output Description

## Input:
The client should provide one comma separated (CSV) file in the below format. Reference file: sample.csv 

- Providers.csv (_REQUIRED_):

|        Column       | Column Required?  |               Meaning                    |
|---------------------|-------------------|------------------------------------------|
| prov_id             |         Y         | Provider ID (NPI)                        |
| prov_spec           |         N         | Provider Specialty                       |
| proc_code           |         Y         | Procedure code (HCPCS, CPT, ICD10, etc.) |
| proc_code_type      |         Y         | Code type                                |
| diag_code           |         Y         | Diagnostic code                          |
| diag_code_type      |         Y         | Diagnostic code type (ICD10 or ICD9)     |--------------------------------------------------------------------------------------
	
## Output:
A list of JSON objects containing the fields listed below. Reference file: sample.csv.out
|   Column   |                         Meaning                          |
|------------|----------------------------------------------------------|
| prov_ID    | Provider's ID                                            |
| prov_clust | Cluster name where vector representing the provider lies |
	
