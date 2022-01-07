FROM python:3.8.2-slim

RUN mkdir -p models templates

COPY app.py .
COPY models/columns.json models/.
COPY models/profit_prediction_model.pkl models/.
COPY templates/index.html templates/.
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
