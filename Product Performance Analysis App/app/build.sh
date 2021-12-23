docker build -t katonic/apps:product-performance-dashboard .
docker push katonic/apps:product-performance-dashboard
# docker run --rm -p 8050:8050 katonic/apps:product-performance-dashboard