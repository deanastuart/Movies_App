Movies Games Web App

I have developed a movie game where players are presented with two actors and guess who has been top billed in more movies.

I’m using The Movie DB to source my data because it is robust, breaks down their data into manageable APIs and there is no limit on the API requests I can make. 

I’ve created a pipeline to fill a MySQL database from TMDB through a series of API requests. You can view that pipeline in API_request_process.py 

The next steps in my apps include
	•   Hosting the website on heroku
	•	Expanding to have users log in and keep track of wins and losses
	•	Add additional games including games where users guess who has been in more movies total, how many movies have two actors been in, and whats an actor’s most popular genre. 
	•	Develop a pipeline for updating the database with new releases
