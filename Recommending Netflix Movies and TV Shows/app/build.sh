docker build -t katonic/apps:movie-recommender .
docker push katonic/apps:movie-recommender
# docker run --rm -p 8050:8050 katonic/apps:movie-recommender