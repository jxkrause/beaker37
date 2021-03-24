"""
module part of beaker37
contains intermediate class that load 'movie_users' from file
or recreates from databse
"""
import pandas as pd
from beaker37.BaseRecommender import BaseRecommender
from beaker37 import library_path

fn_movie_user = library_path + '/models/Recommender_movie_user.csv'
ratings_qu1 = """
select r."userId",m.title  ,avg( r.rating) as rating
from ratings r
join movies m on r."movieId" = m."movieId"
group by r."userId" , m.title
"""


def get_movie_user(engine):
    """
    tries to load 'movie_users' from file
    if file not found recreates file from database
    """
    try:
        movie_user = pd.read_csv(fn_movie_user, index_col=0)
    except FileNotFoundError:
        ratings = pd.read_sql_query(ratings_qu1, engine)
        filt = ratings.groupby('title').transform('count') > 50
        ratings = ratings.loc[filt['userId']]
        movie_user = ratings.pivot(
            index='userId',
            columns='title',
            values='rating')
        movie_user.to_csv(fn_movie_user)
    return movie_user


class MovieUser(BaseRecommender):
    """
    intermediate class that load 'movie_users' from database
    """

    def __init__(self):
        super().__init__()
        self.movie_user = get_movie_user(self.engine)
