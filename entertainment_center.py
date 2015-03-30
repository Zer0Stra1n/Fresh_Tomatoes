#import of necessary modules
import os
import json
import media
import fresh_tomatoes

#Use OS module to create a relative path to the Movie_fake.json file
fn = os.path.join(os.path.dirname(__file__), 'Movie_fake.json')

#have python open the Movie_fake.json file
raw = open(fn)

#Using the JSON module, pull in the data stored in the Movie_fake file
result = json.load(raw)

#new movies_list array to hold each movie
movies_List = []

#for each movie in the Movie_fake.json file
for movie in result['movies']:

    #create a new anonymous Movie instance passing in the necessary args to instantiate it
    #then push that movie into the movie_List array
    movies_List.append(
        media.Movie(movie['title'], movie['plot'], movie['poster'], movie['trailer'], movie['imdbRating'])
    )

#finally, pass the movie_List array to the fresh_tomatoes.open_movies_page function
fresh_tomatoes.open_movies_page(movies_List)
