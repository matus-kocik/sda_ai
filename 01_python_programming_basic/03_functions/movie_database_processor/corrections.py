from data import movies as m
from pprint import pprint


def movieDramas(movies, drama="Drama"):
    list_of_dramas = []
    for movie in movies:
        if drama in movie["genres"]:
            list_of_dramas.append(movie["title"])
    return list_of_dramas


pprint(movieDramas(m, "Comedy"))
pprint(50 * "-")


def findByGenre(genre, movies):
    list_of_movies_by_genre = []
    for movie in movies:
        for movie_by_genre in movie["genres"]:
            if movie_by_genre == genre:
                list_of_movies_by_genre.append(movie["title"])
    return list_of_movies_by_genre


# pprint(findByGenre("Action", m))
pprint(50 * "-")


""" def longestMovie(movies):
    for movie in movies:
        if movie["runtime"] == max([movie["runtime"] for movie in movies]):
            return movie["title"]

pprint(longestMovie(m))
pprint(50 * "-") """


def longestMovies(movies):
    longest_movie = max(movies, key=lambda movie: movie["runtime"])
    return longest_movie["title"]


# pprint(longestMovies(m))
pprint(50 * "-")


def longestMovieByGenre(genre, movies):
    list_of_movies_by_genre = []
    for movie in movies:
        if genre in movie["genres"]:
            list_of_movies_by_genre.append(movie)

    longest_movie = max(list_of_movies_by_genre, key=lambda movie: movie["runtime"])
    return longest_movie["title"]


# pprint(longestMovieByGenre("Comedy", m))
pprint(50 * "-")
