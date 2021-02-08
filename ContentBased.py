import warnings
from sklearn.metrics.pairwise import cosine_similarity
#from AnimeRS.preprocess import *
from Preprocess import *
import numpy as np

def calc_quantile_mean(clean_anime):
    """
    :var quantile: takes the member at 0.75 position in the normal distribution of the data
    :var mean: calculates the average of the rating of each anime.
    """
    quantile = clean_anime.members.quantile(0.75)
    mean = clean_anime.rating.mean()
    return quantile, mean


def weighted_rating(clean_anime, quantile, mean):
    """
    :var term: gets the total users who rated each anime.
    """
    term = clean_anime['members'] / (quantile + clean_anime['members'])
    return clean_anime['rating'] * term + (1 - term) * mean


def get_recommendation(anime_name, cosine_sim, clean_anime, anime_index):
    """
    Getting pairwise similarity scores for all anime in the data frame.
    The function returns the top 10 most similar anime to the given query.
    """
    idx = anime_index[anime_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:11]
    anime_indices = [i[0] for i in sim_scores]
    result = clean_anime[['name']].iloc[anime_indices].drop(idx)
    return result


def cosine_sim(anime_features):
    """
    calculating similarity for each anime with another anime.
    converting to float for easier calculation.
    """
    anime_features_values = anime_features.values.astype(np.float32)
    return cosine_similarity(anime_features_values,anime_features_values)

def check_name(input, clean_anime):
    for name in clean_anime['name']:
        if input == name:
            return True
    return False


def main():
    warnings.filterwarnings("ignore")
    print("\nRunning Content Based")
    clean_anime = load_data('clean_anime.csv')
    check_flag = False

    while not check_flag:
        user_input = input("Enter a name of anime so we can recommend you some similar content: ")
        check_flag = check_name(user_input, clean_anime)
        if not check_flag:
            print("\nEntered name is incorrect or doesn't exist. Please try again.")


    print("Searching...\n")
    quantile, mean = calc_quantile_mean(clean_anime)
    clean_anime['community_rating'] = clean_anime.apply(weighted_rating, axis=1, args=(quantile, mean))
    clean_anime.drop(['anime_id', 'rating', 'members', 'episodes'], axis=1, inplace=True)
    clean_anime.to_csv('clean_anime_CB.csv', index=False)
    clean_anime = pd.concat(
        [clean_anime, clean_anime['type'].str.get_dummies(), clean_anime['genre'].str.get_dummies(sep=',')], axis=1)
    anime_features = clean_anime.loc[:, "Movie":].copy()
    cosine_sim_val = cosine_sim(anime_features)
    anime_index = pd.Series(clean_anime.index, index=clean_anime.name).drop_duplicates()
    results = get_recommendation(user_input.lower(), cosine_sim_val, clean_anime, anime_index)
    results = results['name'].to_string(index=False)

    print(f"similar animes to your choice are:\n\n{results}")
    print("\nFinished Content Based")

