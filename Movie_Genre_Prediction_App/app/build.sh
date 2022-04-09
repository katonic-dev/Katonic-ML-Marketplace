docker build -t katonic/apps:movie-genre-prediction .
docker push katonic/apps:movie-genre-prediction
# docker run --rm -p 8050:8050 katonic/apps:movie-genre-prediction