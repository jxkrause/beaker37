"""
module part of beaker37
contains class recomends moves using user similarities
"""
import pandas as pd
import beaker37.utils as utils
from beaker37.MovieUser import MovieUser

class UserSimilarityRecommender(MovieUser):
    "for recomendation method use similarity"
    def __init__(self):
        super().__init__()

    def recommend(self, user_dict):
        """
        make a recommendation for user input
        user_dict -> dictionary with (parts of) moviename as keys, ratings as values
        returns a list fo movie names
        """
        user_dict = self.translate_user_dict(user_dict)
        new_user = pd.DataFrame(user_dict, index=[-1], columns=self.movie_user.columns, dtype=float)
        # calculate the similarity to each user in your dataset
        similarity = self.movie_user.apply(
            lambda x : utils.euclidian_nan(x.values,new_user.to_numpy()[0]),
            axis=1
            )
        # select the top 5 similar users (sort_values)
        similar_users = similarity.sort_values().head()
        predictions = self.movie_user.loc[similar_users.index].apply(
            lambda x : utils.mean_nan(x,similar_users.to_numpy())
            )
        # recommend some movies
        predictions_ds = predictions.loc[new_user.T.isna().index]
        recomended = list(predictions_ds.sort_values(ascending=False).head().index)
        return self.find_movieId(recomended)

if __name__ == '__main__':
    from beaker37.BaseRecommender import test_movies
    rec = UserSimilarityRecommender()
    print(rec.recommend(test_movies))



