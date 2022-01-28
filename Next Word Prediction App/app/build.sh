docker build -t katonic/apps:next-word-prediction .
docker push katonic/apps:next-word-prediction
# docker run --rm -p 8050:8050 katonic/apps:next-word-prediction