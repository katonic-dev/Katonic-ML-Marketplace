docker build -t katonic/apps:audio-to-text .
docker push katonic/apps:audio-to-text
# docker run --rm -p 8050:8050 katonic/apps:audio-to-text