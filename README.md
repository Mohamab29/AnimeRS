# An anime recommender system 

![Anime](https://escolhasegura.com/wp-content/uploads/2019/03/Melhores-Animes-1.jpg.webp)<br>
In this repositry there is scripts and modules for running the RS and also a notebook that goes throught the whole process from reading the data to giving a recommendation.

## what we have done:

We have built a recommender system for anime based on the given query and if it is in the dataset and using unsupervised learning.<br>
We used two approaches in order to recommend top N anime titles:<br>
* the first approach is based on the content of an anime like genre and type where we turn them into feacture vectors and then comapre them with other titles and check how similar the are to each other
* in the second approach we used the collaborative filtering method where we took the ratings of all the users in the dataset for each anime , so each anime will have a vector of all the users ratings , and in order to choose the most similar titles we used the knn algorithem to give K most similar titles.

## system architecture:
 ....
 
### How to run:
in order to run the scripts you need the following dataset from [kaggle](https://www.kaggle.com/CooperUnion/anime-recommendations-database) or you can download it from the repo
which are anime.csv and rating.csv .





**as you can see there is many csv files which are produced during the running of the scripts**
