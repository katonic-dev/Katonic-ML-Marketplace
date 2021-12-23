FROM python:3.8.2-slim

COPY app.py .
COPY network_traffic_time_series.csv .
COPY finalized_model.sav .
COPY logo.png .
COPY requirements.txt .

RUN apt-get update && apt-get -y install gcc build-essential && pip install -r requirements.txt

CMD streamlit run app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error