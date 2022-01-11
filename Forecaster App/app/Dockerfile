FROM python:3.8.2-slim

RUN mkdir -p static/img static/js static/sampledata static/styles templates

COPY app.py .
COPY helper_v4.py .
COPY static/img/app.png static/img/.
COPY static/img/camera_button.png static/img/.
COPY static/img/csv_file_example.png static/img/.
COPY static/img/csv_icon_blue.png static/img/.
COPY static/img/csv_icon_grey.png static/img/.
COPY static/img/csv_icon_title.png static/img/.
COPY static/img/data-flow.png static/img/.
COPY static/img/download_arrow.png static/img/.
COPY static/img/download_csv.png static/img/.
COPY static/img/export_data.png static/img/.
COPY static/img/facebook_prophet_icon.png static/img/.
COPY static/img/filter_icon.png static/img/.
COPY static/img/forecast_fun.png static/img/.
COPY static/img/forecast_icon.png static/img/.
COPY static/img/forecast_output_example.jpg static/img/.
COPY static/img/heart_opensource.png static/img/.
COPY static/img/heart_opensource_tech.png static/img/.
COPY static/img/loading.gif static/img/.
COPY static/img/mask.png static/img/.
COPY static/img/rocket_features.png static/img/.
COPY static/img/settings_icon_blue.png static/img/.
COPY static/img/settings_icon_grey.png static/img/.
COPY static/img/step1_upload_csv.png static/img/.
COPY static/img/step2_config_settings.png static/img/.
COPY static/img/step2_preforecast_review.png static/img/.
COPY static/img/step3_gen_forecast.png static/img/.
COPY static/img/trend_icon_blue.png static/img/.
COPY static/img/trend_icon_grey.png static/img/.
COPY static/js/behaviour_analytics.js static/js/.
COPY static/js/forecaster_v4.js static/js/.
COPY static/js/jquery-3.3.1.min.js static/js/.
COPY static/js/papaparse.js static/js/.
COPY static/sampledata/annual-sheep-population.csv static/sampledata/.
COPY static/sampledata/example_wp_log_peyton_manning_v2.csv static/sampledata/.
COPY static/sampledata/mean_temps.csv static/sampledata/.
COPY static/sampledata/shampoo_sales.csv static/sampledata/.
COPY static/styles/app.css static/styles/.
COPY static/styles/product_page.css static/styles/.
COPY templates/build-forecast-v3.html templates/.
COPY templates/forecaster.html templates/.
COPY requirements.txt .

RUN apt-get update && apt-get -y install gcc build-essential && pip install -r requirements.txt

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
