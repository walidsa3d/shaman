import tmdbsimple as tmdb
from movie import Movie
tmdb.API_KEY = 'YOUR_API_KEY_HERE'

def search(query):
	search = tmdb.Search()
	results=[]
	response = search.movie(query='The Bourne')
	for s in search.results:
		results.append({'title':s['title'],'id':s['id'],'year':s['year']})
	return results

def get_details(movie_id):
	m=Movie()
	response= tmdb.Movies(movie_id).info()
	m.title=response['title']