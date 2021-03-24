"""
module part of beaker37
base class for Movierecommenders
interfaces to applications
"""
import os
import pandas as pd
from sqlalchemy import create_engine
from fuzzywuzzy import process

class BaseRecommender:
    "base class as interface to web app"
    movies = pd.DataFrame()#contains movies-database for all instances

    def __init__(self):
        self.engine = self.connect_db()
        if BaseRecommender.movies.empty:
            BaseRecommender.movies = pd.read_sql('movies',
                            self.engine,
                            index_col='movieId').drop(columns='index')
        self.movies = BaseRecommender.movies

    def connect_db(self):
        "start db connection"
        psql_uri = os.getenv('PSQL_URI')
        return create_engine(psql_uri, echo=False)

    def find_real_movie_names(self, fuzzy_names):
        "use fuzzywuzzy for exanding movie names"
        return [process.extractOne(x,self.movies['title']) for x in fuzzy_names]

    def translate_user_dict(self, liked_movies):
        "take uses entries passes through fuzzywuzzy"
        real_movies = self.find_real_movie_names(liked_movies)
        real_liked_movies = {}
        for movie,rating in zip(real_movies, liked_movies.values()):
            real_liked_movies[movie[0]] =  int(rating)
        return real_liked_movies

    def find_movieId(self, names):
        "get list of movieIds from movie names"
        ret_val = []
        for name in names:
            filt = self.movies['title'] == name
            movie = self.movies.loc[filt].iloc[0]
            print(movie['title'],movie.name)
            ret_val.append([movie['title'],movie.name])
        return ret_val

    def get_autocomplete_list(self, term):
        "get a list of movie names for autocompletion"
        raw_list = process.extractBests(term, self.movies['title'], limit=5)
        return [x[0] for x in raw_list ]

test_movies = {'Pulp Fiction':4.0,
           'Four Weddings and a Funeral':3.5,
           'Matrix,':0.5,
           'Rashomon':3.5,
           'Trois couleurs: Rouge':4.0
           }
