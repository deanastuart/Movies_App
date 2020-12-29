Movies Games Web App

I’m using The Movie DB to source my data because it is robust, breaks down their data into manageable APIs and there is no limit on the API requests I can make. 

I’ve created a pipeline to fill a MySQL database from TMDB through a series of API requests. I make an api request on an actor’s name and take the response to get their actor id number. I then make another API request to get all of the movies they are in. In a Jupiter notebook, I clean the data by adding “actor name” and “actor id number” columns to the movies table as well as pull out the genres from the list and create a second genre table. I insert these data frames directly into the mysql database that I have created for this project. I am currently filling the database and will refine my method so I can do the entire thing in one python program. 

Next, I would like to create a movies game app that can have some interactive games where users are presented with two actors to guess which one has been first billed in more movies. At this point, I think I will use Flask and Bootstrap as Frameworks and will be supported by MySQL.

Future steps would include:
	
	•	Expanding to have users log in and keep track of wins and losses
	
	•	Add additional games including games where users guess who has been in more movies, how many movies have two actors been in, and whats an actor’s most popular genre. 
	
	•	Develop a pipeline for updating the database with new releases
