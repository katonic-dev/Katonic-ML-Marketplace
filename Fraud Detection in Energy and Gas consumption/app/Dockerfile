FROM python:3.8.2-slim

COPY app.py .
COPY client_train.csv .
COPY invoice_train.csv .
COPY final_model.sav .
COPY logo.png .
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

CMD streamlit run app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
