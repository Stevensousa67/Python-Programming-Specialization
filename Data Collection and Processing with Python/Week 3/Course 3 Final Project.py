# This project will take you through the process of mashing up data from two different APIs to make movie
# recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a
# set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie,
# including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
# You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll
# combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will
# require making API calls to the OMDB API.)

import requests_with_caching
import json


def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    parameters = {}
    parameters['q'] = title
    parameters['type'] = 'movies'
    parameters['limit'] = 5
    tasteDive_data = requests_with_caching.get(url, params=parameters)
    data = json.loads(tasteDive_data.text)
    return data


def extract_movie_titles(data):
    movies = [name['Name'] for name in data['Similar']['Results']]
    return movies


def get_related_titles(lst):
    more_movies = []
    for movie in lst:
        temp_lst = extract_movie_titles(get_movies_from_tastedive(movie))
        for title in temp_lst:
            if title not in more_movies:
                more_movies.append(title)
    return more_movies


def get_movie_data(movie):
    movie_info = {}
    url = 'http://www.omdbapi.com/'
    parameters = {}
    parameters['t'] = movie
    parameters['r'] = 'json'
    omdb_data = requests_with_caching.get(url, params=parameters)
    return json.loads(omdb_data.text)


def get_movie_rating(dict_):
    rating = 0
    for score in dict_['Ratings']:
        if score['Source'] == 'Rotten Tomatoes':
            rating = int(score['Value'][:2])
    return rating


def get_sorted_recommendations(lst):
    movie_list = get_related_titles(lst)
    movie_list = sorted(movie_list, key=lambda movie: (get_movie_rating(get_movie_data(movie)), movie), reverse=True)
    return movie_list
