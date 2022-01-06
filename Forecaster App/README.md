# forecaster

forecaster is a flask web app created with UI on top of Facebook Prophet. It provides the user with a 3 step interface that guides them towards building a baseline forecast with Facebook Prophet:

1. Upload your csv.
2. Configure your initial forecast (choose forecast length and model type - linear or logistic).
3. View Forecast and Tweak settings.

This is a session based product that means this app doesn't store any data about the contents of the uploaded csv within a database. Once the csv has been uploaded to the app, the data is then stored within temporary variables in the client and data is then sent back and forth between client and server until the forecast is generated.

Here is a screenshot of the app after the user has built a forecast:<br/>
<img src="https://raw.githubusercontent.com/katonic-dev/Katonic-ML-Marketplace/master/Forecaster%20App/app/static/img/app.png?token=AQS2G3PLR5NXS5X7KS4CRS3B3VWD6" width="1024" />


### Data Collection on the User Experience

Again, this app does not store any data about the contents of the uploaded csv. I also used the logging python library to suppress any logs echoed during transit between the client and the server.

There is data collected on how people use the app. This data is collected using Google Analytics via a Google Tag Manager implementation. 

At a high level, I use Google Analytics to understand:

1. Whether a user successfully creates a forecast during their session.
2. Whether a user successfully uploads a csv.
3. How a user interacts with different web elements (ie. buttons, links)
4. Whether a user has downloaded a sample csv.
