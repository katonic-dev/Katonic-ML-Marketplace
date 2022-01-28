docker build -t katonic/apps:image-to-text .
docker push katonic/apps:image-to-text
# docker run --rm -p 8050:8050 katonic/apps:image-to-text