from allocine import allocine
from constants import *
from elcinema import elcinema
from imdb import imdby as Imdb
from rotten import rotten
from tmdb import tmdb


def search(query, site):
    if site == "imdb":
        provider = Imdb()
    elif site == "elcinema":
        provider = elcinema()
    elif site == "rottentomatoes":
        provider = rotten(rotten_key)
    elif site == "themoviedatabase":
        provider = tmdb(tmdb_key)
    elif site == "allocine":
        provider = allocine()
    results = provider.search(query)
    return results


def info(movie_id, site):
    if site == "imdb":
        provider = Imdb()
    elif site == "elcinema":
        provider = elcinema()
    elif site == "rottentomatoes":
        provider = rotten(rotten_key)
    elif site == "themoviedatabase":
        provider = tmdb(tmdb_key)
    elif site == "allocine":
        provider = allocine()
    result = provider.info(movie_id)
    return result
