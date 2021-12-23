docker build -t katonic/apps:named-entity-recognizer .
docker push katonic/apps:named-entity-recognizer
# docker run --rm -p 8050:8050 katonic/apps:named-entity-recognizer