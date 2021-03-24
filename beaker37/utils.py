"""
module part of beaker37
helper functions
"""

import numpy as np


def filter_missigs(x1, x2):
    "returns input list only with common not nans"
    filt = np.isnan(x1) | np.isnan(x2)
    x1 = x1[~filt]
    x2 = x2[~filt]
    return (x1, x2)


def cosine_nan(x1, x2):
    "return cosine similartiy"
    x1, x2 = filter_missigs(x1, x2)
    return x1.dot(x2) / np.sqrt(x1.dot(x1)) / np.sqrt(x2.dot(x2))


def pearson_nan(x1, x2):
    "return pearson cimilarity"
    x1, x2 = filter_missigs(x1, x2)
    x1 = x1 - np.mean(x1)
    x2 = x2 - np.mean(x2)
    return cosine_nan(x1, x1)


def euclidian_nan(x1, x2):
    "return euclidian similariy"
    x1, x2 = filter_missigs(x1, x2)
    x3 = x1 - x2
    return 1 / (1 + np.sqrt(x3.dot(x3)))


def mean_nan(x, w):
    "retruns mean not considering nans"
    x = np.array(x)
    filt = np.isnan(x)
    if filt.all():
        return 0
    return np.sum(x[~filt].dot(w[~filt])) / np.sum(w[~filt])
