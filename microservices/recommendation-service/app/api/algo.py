from app.api.service import *
import random

# Fonction renvoyant l'ensemble des id des films vus par un utilisateur donné en paramètre
def ids_movies_watched_by_user(id_user: int) :
    
  watched_movies_user = get_movies_watched_by_user(id_user)
  ids_movies_watched = []
  for usermovie in watched_movies_user :
    ids_movies_watched.append(usermovie.id_movie)
  
  return ids_movies_watched

# Fonction renvoyant l'ensemble des ids des films vus par un groupe d'utilisateurs donné en paramètre
def get_movies_ids(id_group: int):

  users_group = get_usersgroup_by_group(id_group)
  watchmovie_ids = []

  for user in users_group :
    movies_for_user = ids_movies_watched_by_user(user.id)
    for movie_id in movies_for_user :
        watchmovie_ids.append(movie_id)

  return watchmovie_ids

# Fonction calculant les deux plus grandes occurences dans un tableau et renvoyant ces deux occurences
def occurences_max(tab):
    freq = {}
    for num in tab:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max1 = None
    max2 = None
    for num, count in freq.items():
        if max1 is None or count > freq[max1]:
            max2 = max1
            max1 = num
        elif max2 is None or count > freq[max2]:
            max2 = num

    return max1, max2

# Fonction renvoyant 10 éléments aléatoires dans une liste de films donnée en paramètre
def extract_random_elements(movies):
    if len(movies) < 10:
        raise ValueError("List of movies must contain at least 10 elements")
    return random.sample(movies, 10)

# Fonction retournant des recommandations de films à partir de films ayant été vus par un groupe d'utilisateurs passé en paramètre
def recommendations_movies(id_group: int) :
    
  users_group = get_usersgroup_by_group(id_group)

  two_most_view_movie = occurences_max(get_movies_ids(users_group))

  get_all_movie_genre_1 = get_genres_by_movie(two_most_view_movie[0])
  get_all_movie_genre_2 = get_genres_by_movie(two_most_view_movie[1])

  all_genres = get_all_movie_genre_1 + get_all_movie_genre_2

  genre_ids =  []

  for genre in all_genres :
    genre_ids.append(genre.id)

  unique_genres = []
  for genre_id in genre_ids:
      if genre_id not in unique_genres:
        unique_genres.append(genre_id)

  movies_in_genre = []

  movies_view_by_users = get_movies_ids(id_group)

  for genre_id in unique_genres :
    movies_by_idgenre = get_movies_by_genre(genre_id)
    for movie_id in movies_by_idgenre :
      if movie_id.id_movie not in movies_view_by_users :
        movies_in_genre.append(movie_id.id_movie)

  movies_recommanded = extract_random_elements(movies_in_genre)

  return movies_recommanded

