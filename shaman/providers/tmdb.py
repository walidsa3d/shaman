import tmdbsimple as tmd

from models import Movie


class tmdb(object):

    def __init__(self, apikey):
        self.apikey = apikey
        tmd.API_KEY = apikey

    def search(self, query):
        search = tmd.Search()
        results = []
        search.movie(query=query)
        for s in search.results:
            results.append(
                {'title': s['title'], 'id': s['id'], 'year': s['release_date']})
        return results

    def info(self, movie_id):
        movie = Movie()
        response = tmd.Movies(movie_id).info()
        movie.title = response['title']
        movie.plot = response['overview']
        movie.year = response['release_date'].split('-')[0]
        return movie
