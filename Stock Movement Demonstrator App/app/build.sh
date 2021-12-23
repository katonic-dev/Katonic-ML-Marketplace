docker build -t katonic/apps:stock-movement-app .
docker push katonic/apps:stock-movement-app
# docker run --rm -p 8050:8050 katonic/apps:stock-movement-app