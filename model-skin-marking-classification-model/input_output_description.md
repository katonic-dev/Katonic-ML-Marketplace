# Input/Output Description

- Input: 1 image in .jpg, .bmp or .png format. **__Reference file: input.jpg__**

## Output
- Output: a JSON object containing probability value between 0 - 1 indicating the likelihood of BCC or SCC skin cancer**__Reference file: input.jpg.out__**
    - Columns:
        - Image: name of input image file
        - BCC: probability of BCC skin cancer
        - Other: probability of other skin cancer
