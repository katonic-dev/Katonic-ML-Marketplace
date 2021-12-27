# Flight_Delay_Prediction
This solution predicts flight delays based on factors such as route, airport congestion, airline diversion etc. using a trainable ML model.

## Product overview
Flight delays could cause airlines to incur financial losses in the form of accommodation expenses for the delayed passengers as well as penalties, fines, and operational costs for aircraft labour retention at airports. Furthermore, continual unexpected delays could cause the airline to lose their customers. 

This solution predicts whether a flight would be delayed at the origin airport and by how many minutes. It utilizes latent factors such as flight route, airport congestion, airline diversion and temporal features derived from U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics data on flight on-time performance for large air carriers. The solution uses Random Forest model to capture and predict on-time behaviour of commercial flights.

## Product Highlight 
* The solution uses latent airport and airline specific operational features obtained from standardized U.S. DoT flight on-time performance data. The solution can be trained on client data to capture and predict client specific operational patterns.
* Delay in a flight causes subsequent flights to be delayed causing the aircraft and crew schedules to be negatively impacted. Being able to predict the delay allows for better operational planning at the destination airport based on expected flight delay at origin. It also allows for better customer communication in providing flight recommendations for multi-leg journeys and avoid potential over-scheduling.
