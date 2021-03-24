"""
module part of beaker37
contains class recomends moves useing non-negative matrix factorization
"""
import pickle
import pandas as pd
from sklearn.decomposition import NMF
from beaker37.MovieUser import MovieUser
from beaker37 import library_path

fn_sklearn_model = library_path + '/models/NMF_model.p'


class NMFRecommender(MovieUser):
    "for recomendation method non-negative matrix factorization"

    def __init__(self):
        super().__init__()
        self.mean_movie_rating = self.movie_user.mean(axis=0)
        self.movie_user.fillna(self.mean_movie_rating, inplace=True)
        try:
            with open(fn_sklearn_model, "rb") as fp:
                self.model = pickle.load(fp)
        except FileNotFoundError:
            self.model = NMF(init='random', n_components=30, max_iter=1000)
            self.model.fit(self.movie_user)
            with open(fn_sklearn_model, 'wb') as fp:
                pickle.dump(self.model, fp)

    def recommend(self, user_dict):
        """
        make a recommendation for user input
        user_dict -> dictionary with (parts of) moviename as keys, ratings as values
        returns a list fo movie names
        """
        user_dict = self.translate_user_dict(user_dict)
        new_user = pd.DataFrame(user_dict,
                                index=[-1],
                                columns=self.movie_user.columns,
                                dtype=float)
        new_user.fillna(self.mean_movie_rating, inplace=True)
        p_matrix = self.model.transform(new_user)
        q_matrix = self.model.components_
        ds = pd.Series(
            p_matrix.dot(q_matrix)[0],
            index=self.movie_user.columns).sort_values()
        return self.find_movieId(list(ds.tail(5).index))


if __name__ == '__main__':
    from beaker37.BaseRecommender import test_movies
    rec = NMFRecommender()
    print(rec.recommend(test_movies))
