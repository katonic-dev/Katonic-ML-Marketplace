docker build -t katonic/apps:late-shipment-prediction .
docker push katonic/apps:late-shipment-prediction
# docker run --rm -p 8050:8050 katonic/apps:late-shipment-prediction