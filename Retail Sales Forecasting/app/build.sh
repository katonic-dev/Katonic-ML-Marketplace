docker build -t katonic/apps:retail-sales-forecast .
docker push katonic/apps:retail-sales-forecast
# docker run --rm -p 8050:8050 katonic/apps:retail-sales-forecast