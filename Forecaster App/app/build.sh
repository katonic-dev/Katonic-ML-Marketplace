docker build -t katonic/apps:forecaster .
docker push katonic/apps:forecaster
# docker run --rm -p 8050:8050 katonic/apps:forecaster