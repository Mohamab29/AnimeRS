# from AnimeRS.Preprocess import *
from Preprocess import *

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import numpy as np


def filter_rating(rating):
    anime_ratings_count = rating.groupby(by='anime_id').count()['rating'].reset_index().rename(
        columns={'rating': 'rating_count'})
    user_rating_count = rating.groupby(by='user_id').count()['rating'].reset_index().rename(
        columns={'rating': 'rating_count'})
    return anime_ratings_count,user_rating_count


def filter_tables(df_count,num):
    return df_count[df_count['rating_count'] > num]


def join_tables(filter_anime_rating, filter_user_rating, rating):
    filtered_rating_anime = rating[rating['anime_id'].isin(filter_anime_rating['anime_id'])]
    filtered_rating = filtered_rating_anime[filtered_rating_anime['user_id'].isin(filter_user_rating['user_id'])]
    return filtered_rating


def convert_to_matrix(joined_table):
    """
    converting table to matrix for easier access to data.
    """
    rating_matrix = joined_table.pivot_table(index='anime_id', columns='user_id', values='rating').fillna(0)
    csr_rating_matrix = csr_matrix(rating_matrix.values)
    return rating_matrix, csr_rating_matrix


def KNN(csr_rating_matrix):
    knn_model = NearestNeighbors(metric='cosine')
    knn_model.fit(csr_rating_matrix)
    return knn_model


def check_name(input, clean_anime):
    print("in check name")

    for name in clean_anime['name']:
        if input == name:
            return True
    return False


def main():
    print("\nRunning NN")
    rating = load_data('rating.csv')
    anime = load_data('clean_anime.csv')
    check_flag = False

    while not check_flag:
        print("getting input\n")
        user_input = input("Enter a name of anime so we can recommend you some similar content: ")
        check_flag = check_name(user_input, anime)
        print("got checked\n")
        if not check_flag:
            print("\nEntered name is incorrect or doesn't exist. Please try again.")

    print("Searching...\n")

    anime_ratings_count, user_rating_count = filter_rating(rating)
    anime_ratings_count.to_csv('clean_rating_NN.csv', index=False)
    filter_anime_rating= filter_tables(anime_ratings_count,250)
    filter_user_rating = filter_tables(user_rating_count,100)
    joined_table = join_tables(filter_anime_rating,filter_user_rating, rating)
    rating_matrix, csr_rating_matrix = convert_to_matrix(joined_table)
    model = KNN(csr_rating_matrix)
    user_anime = anime[anime['name'] == user_input.lower()]
    user_anime_index = np.where(rating_matrix.index == int(user_anime['anime_id']))[0][0]
    user_anime_ratings = rating_matrix.iloc[user_anime_index]
    user_anime_ratings_reshaped = user_anime_ratings.values.reshape(1,-1)
    distances, indices = model.kneighbors(user_anime_ratings_reshaped, n_neighbors=11)
    nearest_neighbors_indices = rating_matrix.iloc[indices[0]].index[1:]
    nearest_neighbors = pd.DataFrame({'anime_id': nearest_neighbors_indices})
    top_10_reco = pd.merge(nearest_neighbors, anime,on='anime_id',how='left')
    top_10_reco = top_10_reco['name'].to_string(index=False)

    print(f"similar animes to your choice are:\n\n{top_10_reco}")

    print("\nFinished NN")





