"""
module part of beaker37
contains class that randomly recomends moves 
"""
import random
from beaker37.BaseRecommender import BaseRecommender

class RandomRecommender(BaseRecommender):
    "contains class that randomly recomends moves "
    def __init__(self):
        super().__init__()

    def recommend(self, user_dict):
        """
        returns a verified list of movies
        user_dict -> dictionary with (parts of) moviename as keys, ratings as values
        returns a list fo movie names
        """
        user_dict = self.translate_user_dict(user_dict)
        rnd_movie_ids = random.choices(self.movies['title'].apply(
            lambda x : x not in user_dict.keys()).index,k=5
            )
        lst = list(self.movies.loc[rnd_movie_ids]['title'])
        return self.find_movieId(lst)


if __name__ == '__main__':
    from beaker37.BaseRecommender import test_movies
    rec = RandomRecommender()
    print(rec.recommend(test_movies))
