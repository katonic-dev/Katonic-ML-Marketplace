# Input/Output Description
- Input:
> Note: Data at the claims level (each bullet point is a field); all keys must be present, values may be null when specified
- Providers.csv (_REQUIRED_):

|        Column       |  Column Required?  |                   Meaning                     |
|---------------------|--------------------|-----------------------------------------------|
| prov_id             |         Y          | Provider ID (NPI)                             |
| prov_spec_id        |         Y          | Provider specialty ID                         |
| proc_code           |         Y          | Procedure code                                |
| proc_code_type      |         Y          | Procedure Code type (HCPCS, CPT, ICD10, etc.) |
	
- Output: a JSON list of objects contaning, for each record in the original orderthe following fields:
	- prov_id        : Provider ID                      
	- proc_code      : Procedure code                                                                 
	- proc_code_type : Procedure Code type (HCPCS, CPT, ICD10, etc.)                                  
	- risk_score     : Provider's risk score (provider's likelihood that procedure code is erroneous) 
 - Reference file: sample.zip.out	
	
