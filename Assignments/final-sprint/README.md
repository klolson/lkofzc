# Film Review Web App

## How to run final-project
+ Install sails with the following command: npm install sails -g
+ Clone the lkofzc repository onto your machine
+ Navigate to the final-project folder in the repository (lkofzc/Assignments/final-sprint/final-project): cd final-project
+ Run the application with the following command: sails lift
+ Go to localhost:1337 in your browser to view the page. You should be able to create a user and login to the application

## Project Overview
+ A web app that will allow registered users to submit their own reviews of movies as well as view the reviews of others
+ Utilizes the sails web framework to organize the site into a MVC architecture
+ Users must have a registered account to view and create movie reviews

## What Works
+ A list of created film reviews will be displayed upon logging in
+ A film review can be created by clicking on the add button
+ The app saves account information and allows a registered user to login

## Problems I ran into
+ I ran into serious issues handleing POST requests in the app, I don't have much experience with backend so it was hard for me to create the api and pass information between different pages
+ I think some of my issues stem from the fact that I didn't create an actual database, I was merly using local storage to temporarily store the information being created. Perhaps if I used something like mongoDB it would be easier to pass information back and forth.
+ For some reason when a new movie review is created the server crashes and the web app must be restarted. The strange thing about this is that the movie review is still created and upon resetting the web app the movie review can seen successfully created
  + For testing purposes a film review can be manually created by typing the following in the url localhost:1337/reviews/Create?title=Review One&body=Sample test
  + Using this method does not crash the web app, so I believe there is an issue with my POST request in the project. I believe it is a problem with a CSRF token that needs to be passed with every POST request for security purposes: https://sailsjs.com/documentation/concepts/security/csrf
  
## Resources that I used
+ I primarily used the sails documentation from their website: https://sailsjs.com/documentation/reference
+ I looked at many different potential database options: https://sailsjs.com/documentation/concepts/extending-sails/adapters/available-adapters
  + I experimented with mongoDB the most, but I don't have much database experience so I was finding it very hard to get the credentials set up properly
  + I decided for my purposes I would use the default localdisk available in sails to serve as a temp database info on this can be found here: https://www.npmjs.com/package/sails-disk
+ I used bootstrap to help build the UI: https://getbootstrap.com/

## What I learned
+ The project in its current state is very messy, but I feel I have a much stronger knowledge as to how sails works and how to buidl a sails app
+ I have more of a grasp as to how get and post request works, I sort of succeeded in passing information correctly between pages
+ I was able to get an SSO set up easily following sails tutorials.
