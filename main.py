import string

import pandas as pd
import string


def load_data():
    anime = pd.read_csv('anime.csv')
    rating = pd.read_csv('rating.csv')
    return anime, rating


def clean_data(anime):
    '''
    symbol &#039; means '. replaced it with 1 so we will bw able to distinguish the difference.
    '''
    anime["name"] = anime["name"].str.replace('&#039;', '\'')
    anime["name"] = anime["name"].str.replace('\'', '1')
    anime["name"] = anime["name"].str.replace('[^\s\w]', '')
    return anime

def fill_missing_data(anime):
    # anime.loc[(anime["genre"] == "Hentai") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    anime.loc[(anime["type"] == "OVA") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    anime.loc[(anime["type"] == "Movie") & (anime["episodes"] == "Unknown")] = "1"
    anime.loc[(anime["type"] == "TV") & (anime["episodes"] == "Unknown")] = "1"
    anime.loc[(anime["type"] == "Music") & (anime["episodes"] == "Unknown")] = "1"
    anime.loc[(anime["type"] == "ONA") & (anime["episodes"] == "Unknown")] = "1"
    anime = anime[anime['type'].notna()]
    anime["rating"].fillna(anime["rating"].median()-1, inplace=True)

    anime["members"] = anime["members"].astype(float)
    return anime




anime, rating = load_data()
anime = clean_data(anime)
anime = fill_missing_data(anime)
anime.to_csv("clean_anime.csv")
