# Recommending Netflix Movies and TV Shows App

This app Recommends Netflix movies based on the user searches.

## Product Overview

* There are several methods to create a list of Recommendations according to your preferences.
You can use the preferences of other users that have seen the same contents (Collaborative-filtering) as you or you can find the contents that are the closest to the one you liked before (Content-based Filtering). 

* In this App we are using Content-based Filtering to recommend movies to the user.

* To find the similarity we can compare the features from the movies: for example 
the actors, the director, the genre, the synopsis, etc. In order to measure the distance
between the vectors formed by the features we can use **Cosine Similarity**.
