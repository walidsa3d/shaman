from imdbpie import Imdb
from models import Movie


class imdby:

    def __init__(self):
        self.imdb = Imdb(anonymize=True, cache=True)

    def search(self, query):
        results = []
        for result in self.imdb.search_for_title(query):
            results.append(
                {'title': result['title'], 'year': result['year'], 'id': result['imdb_id']})
        return results

    def info(self, movie_id):
        title = self.imdb.get_title_by_id(movie_id)
        movie = Movie()
        movie.title = title.title
        movie.rating = unicode(title.rating)
        movie.plot = title.plot_outline
        movie.year = title.year
        return movie
