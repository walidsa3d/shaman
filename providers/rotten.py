from rottentomatoes import RT


class rotten:
	def __init__(self):
		self.rt=RT("api_key")
	def search(self,query):
		print rt.search(query)

	def get_details(self,movie_id):
		rt.info(movie_id)