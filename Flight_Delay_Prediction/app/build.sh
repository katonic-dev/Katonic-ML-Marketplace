docker build -t katonic/apps:flight-delay-prediction .
docker push katonic/apps:flight-delay-prediction
# docker run --rm -p 8050:8050 katonic/apps:flight-delay-prediction