from AnimeRS.preprocess import *


def calc_quantile_mean(anime):
    """
    :var quantile: takes the member at 0.75 position in the normal distribution of the data
    :var mean: calculates the average of the rating of each anime.
    """
    quantile = anime.members.quantile(0.75)
    mean = anime.rating.mean()
    return quantile, mean


def weighted_rating(anime,quantile,mean):
    """
    :var term: gets the total users who rated each anime.
    :return : calculation of the weighted rating of each anime.
    """
    term = anime['members'] / (quantile + anime['members'])
    return anime['rating'] * term + (1 - term) * mean


