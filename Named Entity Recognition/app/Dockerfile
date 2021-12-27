FROM python:3.8.2-slim

COPY requirements.txt .
RUN pip install -r requirements.txt && python -m spacy download en_core_web_sm && rm requirements.txt

# COPY models/columns.json .
# COPY models/profit_prediction_model.pkl .
COPY app.py .
COPY templates/index.html .
COPY templates/preview.html .
COPY templates/previewer.html .
COPY templates/result.html .

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error