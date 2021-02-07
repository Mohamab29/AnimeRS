import preprocess


def calc_quantile_mean(anime):
    '''
    Quantile (0.75) takes the member at 0.75 position in the normal distribution of the data
    '''
    quantile = anime.members.quantile(0.75)
    mean = anime.rating.mean()
    return quantile, mean

# def weighted_rating(anime,quantile,mean):