docker build -t katonic/apps:fraudulent-claim-detection .
docker push katonic/apps:fraudulent-claim-detection
# docker run --rm -p 8050:8050 katonic/apps:fraudulent-claim-detection