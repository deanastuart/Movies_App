import requests
import json
from sqlalchemy import create_engine
import os
import pandas as pd

api_key=os.getenv('API_KEY')
pw=os.getenv('MYSQL')
str_sql='mysql+mysqlconnector://root:'+pw+'@localhost/movies'
engine=create_engine(str_sql)
with engine.connect() as connection:
    con = connection.execute

# Loop to prepare actor name for API request
def request_actor_id(actor):
    #actor = 'Jack Nicholson'
    actor_name = ''
    for i in actor:
        if i == ' ':
            i = '%20'
            actor_name += i
        else:
            actor_name += i

    actor_request_url = "https://api.themoviedb.org/3/search/person?api_key=" + str(api_key)+"&language=en-US&query=" + str(
        actor_name) + "&include_adult=false"

    response = requests.request("GET", actor_request_url)

    # reading the response and pulling out the list in the dictionary
    response = response.json()
    response = response['results']
    response = response[0]

    # pulling out the actor id
    actor_id = response['id']
    print(actor +" ID: " + str(actor_id))

    #make the request for movies
    request_url = "https://api.themoviedb.org/3/person/" + str(
        actor_id) + "/movie_credits?api_key=" + str(api_key) + "&language=en-US"

    #format the response
    movies = requests.request('GET', request_url)
    movies = movies.json()

    movies = movies.get('cast')

    #add columns for the actor name and the actor id
    for i in movies:
        i.update({"actor_name": str(actor), "actor_id": str(actor_id)})


    movies = pd.DataFrame(movies)

    #pull out the genres into its own dataframe
    genres = movies[["id", "genre_ids"]].copy()
    genres = genres.explode('genre_ids')
    movies = movies.drop(["genre_ids"], axis=1)

    #add the movies and genre dataframes into mysql
    movies.to_sql('movies', con=engine, if_exists='append')
    genres.to_sql('genres', con=engine, if_exists='append')


if __name__ == "__main__":
    list = ['Rachel Weisz','Jessica Chastain','Julia Roberts','Nicole Kidman',
            'Reese Witherspoon','Sarah Paulson','Jessica Lange','Anne Hathaway',
            'Sigourney Weaver','Scarlett Johansson','Emilia Clarke','Jodie Foster',
            'Michelle Pfeiffer','Charlize Theron']
    for i in list:
        request_actor_id(i)
