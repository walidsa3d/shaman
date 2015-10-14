import requests

from bs4 import BeautifulSoup as bs
from models import Movie
from pyquery import PyQuery


class elcinema(object):

    def __init__(self):
        self.base_url = 'http://www.elcinema.com/'

    def search(self, query):
        search_url = self.base_url + \
            'search/?search_for=%s&category=work' % query
        response = requests.get(search_url).text
        soup = bs(response, "lxml")
        s = soup.find_all('div', attrs={'class': 'media-photo'})
        results = []
        for r in s:
            title = unicode(r.find_all('a')[2].text)
            id = r.find_all('a')[2].get('href').split('/')[2]
            results.append({'title': title, 'id': id, 'year': ''})
        return results

    def info(self, movie_id):
        movie_url = self.base_url+'work/'+movie_id
        response = requests.get(movie_url).text
        movie = Movie()
        soup = bs(response, "lxml")
        movie.title = soup.find(attrs={'itemprop': 'name'}).text
        movie.plot = soup.find(attrs={'itemprop': 'description'}).text
        movie.year = soup.select("ul.unstyled > li")[2].find_all('a')[1].text
        return movie
