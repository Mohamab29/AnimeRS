import string

import pandas as pd
import string


def load_data(dataframe):
    df = pd.read_csv(dataframe)
    return df


def clean_data(anime):
    '''
    symbol &#039; means '. replaced it with 1 so we will bw able to distinguish the difference.
    '''
    anime["name"] = anime["name"].str.replace('&#039;', '\'')
    anime["name"] = anime["name"].str.replace('\'', '1')
    anime["name"] = anime["name"].str.replace('[^\s\w]', '')
    return anime

def fill_missing_data(anime):
    '''
    making data clearer and changing UNKNOWN values to 1 for better data usage.
    '''
    anime.loc[(anime["type"] == "OVA") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    anime.loc[(anime["type"] == "Movie") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    anime.loc[(anime["type"] == "TV") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    anime.loc[(anime["type"] == "Music") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    anime.loc[(anime["type"] == "ONA") & (anime["episodes"] == "Unknown"), "episodes"] = "1"
    '''
    this command is used once only. used to clean values of ' ' from genre column.
    '''
    # anime.drop(anime.loc[(anime['genre'] == " ")])
    '''
    NONE types are removed from df.
    '''
    anime = anime.loc[anime['type'].notna()]
    '''
    anime without rating is changed to median rating.
    '''
    madian = anime["rating"].median()-1
    anime["rating"].fillna(madian, inplace=True)

    # anime["members"] = anime["members"].astype(float)
    return anime





def main():
    anime = load_data('anime.csv')
    # rating = load_data('rating.csv')
    anime = clean_data(anime)
    anime = fill_missing_data(anime)
    anime.to_csv('clean_anime.csv', index=False)
    clean_anime = load_data('clean_anime.csv')

main()