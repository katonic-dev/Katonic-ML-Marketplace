FROM python:3.8.2-slim

COPY app.py .
COPY models/columns.json .
COPY models/profit_prediction_model.pkl .
COPY templates/index.html .
COPY requirements.txt .

RUN python -m spacy download en_core_web_sm
RUN pip install -r requirements.txt

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error