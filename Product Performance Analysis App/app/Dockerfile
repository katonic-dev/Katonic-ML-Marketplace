FROM python:3.8.2-slim

COPY app.py .
COPY final_ads_till_Aug.csv .
COPY final_data_till_Aug_Flag_with_adj_1.csv .
COPY final_output_Oct_final.csv .
COPY assets/fashion_mnist.css .
COPY assets/logo.png .
COPY requirements.txt .

RUN apt-get update && apt-get -y install gcc build-essential && pip install -r requirements.txt

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error