docker build -t katonic/apps:bank-customer-churn .
docker push katonic/apps:bank-customer-churn
# docker run --rm -p 8050:8050 katonic/apps:bank-customer-churn