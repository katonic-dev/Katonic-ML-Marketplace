FROM python:3.8.2-slim

COPY app.py .
COPY logo.png .
COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y && apt-get install -y git
RUN pip install -e git+https://github.com/ehsanbehdad/Pytube#egg=pytube
RUN pip install -r requirements.txt

CMD streamlit run app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
