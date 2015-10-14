from models import Movie
from rottentomatoes import RT


class rotten(object):

    def __init__(self, apikey):
        self.api_key = apikey
        self.rt = RT(self.api_key)

    def search(self, query):
        results = []
        for result in self.rt.search(query):
            results.append(
                {'title': result['title'], 'year': result['year'], 'id': result['id']})
        return results

    def info(self, movie_id):
        m = Movie()
        data = self.rt.info(movie_id)
        m.plot = data['synopsis']
        m.title = data['title']
        m.year = data['year']
        return m
