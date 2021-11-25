# Input/Output Description

- Input: 1 comma separated (csv) file. **__Reference file: request.csv__**
- Details for each csv file:
    - request.csv (required)
        - Required columns: 
            - case_id: case identifier
            - subject: case subject
            - description: case description
            - chat_body: chat transcripts from the help desk



## Output
- Output: a comma separated csv file containing the predicted customer intent on case_id.  **__Reference file: request.csv.out__**
    - Columns:
        - case_id: case identifier
        - stage: classified stage of the case lifetimecycle
        - customer_intent: predicted customer intent
