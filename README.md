# An anime recommender system 

![Anime](https://escolhasegura.com/wp-content/uploads/2019/03/Melhores-Animes-1.jpg.webp)<br>

## what we have done:

We have built a recommender system for anime based on the given query (anime title) and if it is in the dataset and using unsupervised learning.<br>
We used two approaches in order to recommend top N anime titles:<br>
* the first approach is based on the content of an anime like genre and type where we turn them into feature vectors and then comapre them with other titles and check how similar they are to each other
* in the second approach we used the collaborative filtering method where we took the ratings of all the users in the dataset for each anime , so each anime will have a vector of all the users ratings , and in order to choose the most similar titles we used the knn algorithem to give K most similar anime to the query.

 
### How to run:
in order to run the scripts you need the following dataset from [kaggle](https://www.kaggle.com/CooperUnion/anime-recommendations-database) or you can download it from the repo
which are **anime.csv** and **rating.csv** and you need to put them in the same directory as the four python scrtips (main,preprocessing,contentbased,NearestNeighbor).

run the main script and a menu will pop up :

 ![Architecture](https://raw.githubusercontent.com/Mohamab29/AnimeRS/main/AnimeRS-Data/menu.png)<br>

run the preprocess choice:

 ![Architecture](https://raw.githubusercontent.com/Mohamab29/AnimeRS/main/AnimeRS-Data/choice1.png)<br>
 
 after the preprocessing is done ,  a new cleaned csv file is saved in the local directory which is used throught the program.
 Now you can choose to run one the recommender system and after that enter an anime title and get the recommendations :)
 
 ![Architecture](https://raw.githubusercontent.com/Mohamab29/AnimeRS/main/AnimeRS-Data/choice2.png)<br>

## system architecture:

 ![Architecture](https://raw.githubusercontent.com/Mohamab29/AnimeRS/main/AnimeRS-Data/system-architecture.jpg)<br>

## some notes:
The **AnimeRS.ipynb** is our EDA notebook where you can see the data and how we wrote the different processes ...

The system needs to be modified into a hybrid personalised kind of recommender in order to give more accurate and personalised result. 

