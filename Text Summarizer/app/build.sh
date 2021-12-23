docker build -t katonic/apps:text-summarizer .
docker push katonic/apps:text-summarizer
# docker run --rm -p 8050:8050 katonic/apps:text-summarizer