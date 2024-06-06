import pandas as pd

#with open('./data/movies.csv', 'rb') as f:
#  movies = f.read()

movies = pd.read_csv('./data/movies.csv')
ratings = pd.read_csv('./data/ratings.csv')  

# Removing duplicate rows
movies.drop_duplicates(inplace=True)
ratings.drop_duplicates(inplace=True)

# removing missing values
movies.dropna(inplace=True)
ratings.dropna(inplace=True)

print('first:', movies.iloc[0])

from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors # Using Nearest Class from scikit-learn 

def process_data():
  
  genres = movies['genres'] # feature (column) to be based on
  
  
  encoder = OneHotEncoder() # instanciate the encoder
  genres_encoded = encoder.fit_transform(genres.values.reshape(-1, 1)) # fitting and transforming the generes column
  
  #print('genres:', genres)
  #print('genres_encoded:', genres_encoded)
  
  recommender = NearestNeighbors(metric='cosine') # we're using the cosine metric 
  recommender.fit(genres_encoded.toarray())
  
  return recommender, genres_encoded
    
def recommend_movie(movie_index):
  recommender, genres_encoded = process_data()
  
  #movie_index = index # the movie the user has previously watched
  num_recommendations = 25 # number of recommendations to return
  
  # getting the recommendations
  _, recommendations = recommender.kneighbors(genres_encoded[movie_index].toarray(), n_neighbors=num_recommendations)

  # extracting the movie titles from the recommendations
  recommend_movie_titles = movies.iloc[recommendations[0]] #['title']
  
    
  print('movie_based_on:', movies.iloc[movie_index])
  print('\nrecommendations:',recommend_movie_titles)

recommend_movie(0)  
  

#print(movies)
#print(ratings)