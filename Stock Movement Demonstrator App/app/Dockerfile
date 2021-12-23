FROM python:3.8.2-slim

COPY app.py .
COPY assets/logo.png .
COPY templates/index3.html .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD streamlit run app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error