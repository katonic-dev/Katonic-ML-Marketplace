FROM python:3.8.2-slim

COPY app.py .
COPY helper_v4.py .
COPY static\img\app.png .
COPY static\img\camera_button.png .
COPY static\img\csv_file_example.png .
COPY static\img\csv_icon_blue.png .
COPY static\img\csv_icon_grey.png .
COPY static\img\csv_icon_title.png .
COPY static\img\data-flow.png .
COPY static\img\download_arrow.png .
COPY static\img\download_csv.png .
COPY static\img\export_data.png .
COPY static\img\facebook_prophet_icon.png .
COPY static\img\filter_icon.png .
COPY static\img\forecast_fun.png .
COPY static\img\forecast_icon.png .
COPY static\img\forecast_output_example.jpg .
COPY static\img\heart_opensource.png .
COPY static\img\heart_opensource_tech.png .
COPY static\img\loading.gif .
COPY static\img\mask.png .
COPY static\img\rocket_features.png .
COPY static\img\settings_icon_blue.png .
COPY static\img\settings_icon_grey.png .
COPY static\img\step1_upload_csv.png .
COPY static\img\step2_config_settings.png .
COPY static\img\step2_preforecast_review.png .
COPY static\img\step3_gen_forecast.png .
COPY static\img\trend_icon_blue.png .
COPY static\img\trend_icon_grey.png .
COPY static\js\behaviour_analytics.js .
COPY static\js\forecaster_v4.js .
COPY static\js\jquery-3.3.1.min.js .
COPY static\js\papaparse.js .
COPY static\sampledata\annual-sheep-population.csv .
COPY static\sampledata\example_wp_log_peyton_manning_v2.csv .
COPY static\sampledata\mean_temps.csv .
COPY static\sampledata\shampoo_sales.csv .
COPY static\styles\app.css .
COPY static\styles\product_page.css .
COPY templates\build-forecast-v3.html .
COPY templates\forecaster.html .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error