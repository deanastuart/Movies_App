import requests
from sqlalchemy import create_engine
import os
import pandas as pd

api_key=os.getenv('API_KEY')
username = os.getenv('MYSQL_user')
pw=os.getenv('MYSQL')
str_sql='mysql+mysqlconnector://'+username+':'+ pw +'@localhost/movies'
engine=create_engine(str_sql)
with engine.connect() as connection:
    con = connection.execute

# Loop to prepare actor name for API request
def request_actor_id(actor):
    actor_name = ''
    for i in actor:
        if i == ' ':
            i = '%20'
            actor_name += i
        else:
            actor_name += i

    #first api request to get the actor id number
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

    #rename character and order columns and add an actor and movies column as the primary ke
    movies = movies.rename(columns={"character": "movie_character", "order": "billing_order"})
    movies['actor_and_movie'] = movies[['actor_name', 'id']].apply(lambda x: ' '.join(x.map(str)), axis=1)

    #add the movies and genre dataframes into mysql
    movies.to_sql('movies', con=engine, if_exists='append', index=False)
    genres.to_sql('genres', con=engine, if_exists='append', index=False)


if __name__ == "__main__":
    #by providing a list of actors, I can add
    list = ['Tim Roth', 'Bruce Willis', 'Marylin Monroe']
    for i in list:
        request_actor_id(i)
