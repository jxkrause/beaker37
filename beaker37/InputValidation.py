"""
module part of beaker37
contains class that translate user input to existing movie names
"""
from beaker37.BaseRecommender import BaseRecommender

class InputValidation(BaseRecommender):
    "class that translate user input to existing movie names"
    def __init__(self):
        super().__init__()

    def recommend(self, user_dict):
        """
        returns a verified list of movies
        user_dict -> dictionary with (parts of) moviename as keys, ratings as values
        returns a list fo movie names
        """
        user_dict = self.translate_user_dict(user_dict)
        return self.find_movieId(list(user_dict.keys()))


if __name__ == '__main__':
    from beaker37.BaseRecommender import test_movies
    rec = InputValidation()
    print(rec.recommend(test_movies))
