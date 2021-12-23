docker build -t katonic/apps:network-traffic-forecast .
docker push katonic/apps:network-traffic-forecast
# docker run --rm -p 8050:8050 katonic/apps:network-traffic-forecast