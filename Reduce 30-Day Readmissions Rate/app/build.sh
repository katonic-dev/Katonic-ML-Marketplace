docker build -t katonic/apps:reduce-readmissions-rate .
docker push katonic/apps:reduce-readmissions-rate
# docker run --rm -p 8050:8050 katonic/apps:reduce-readmissions-rate