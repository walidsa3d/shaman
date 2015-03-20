from imdbpie import Imdb
from movie import Movie

class imdby:
	def __init__(self):
		self.imdb=Imdb(anonymize=True,cache=True)
	def search(self,query):
		results=[]
		for result in self.imdb.search_for_title(query):
			results.append({'title':result['title'],'year':result['year'],'id':result['imdb_id']})
		return results

	def get_details(self,movie_id):
		title=self.imdb.get_title_by_id(movie_id)
		movie=Movie()
		movie.title=title.title
		movie.year=unicode(title.rating)
		movie.plot=title.plots[0]
		return movie

if __name__ == '__main__':
	print imdby().search("love")


