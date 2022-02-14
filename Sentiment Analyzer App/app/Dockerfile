FROM python:3.8.2-slim

RUN pip install -r requirements.txt

COPY app.py .
COPY logo.png .
COPY requirements.txt .

CMD streamlit run app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error