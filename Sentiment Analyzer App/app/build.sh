docker build -t katonic/apps:sentiment-analyzer .
docker push katonic/apps:sentiment-analyzer
# docker run --rm -p 8050:8050 katonic/apps:sentiment-analyzer