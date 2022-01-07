FROM python:3.8.2-slim

COPY app.py .
COPY client_train.csv .
COPY invoice_train.csv .
COPY final_model.sav .
COPY logo.png .
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && apt-get -y install curl && apt-get install libgomp1 && pip install -r requirements.txt

CMD streamlit run app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
