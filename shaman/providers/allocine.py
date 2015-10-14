import json
import requests

from models import Movie


class allocine(object):

    def __init__(self):
        self.base_url = 'http://api.allocine.fr/rest/v3/search'
        self.info_url = "http://api.allocine.fr/rest/v3/movie?partner=YW5kcm9pZC12M3M&code=61282&format=json&filter=movie&striptags=synopsis,synopsisshort"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'}

    def search(self, query):
        payload = {'partner': 'YW5kcm9pZC12M3M', 'filter': 'movie', 'count': 30, 'page': 1,
                   'q': query, 'format': 'json'}
        #req = requests.Request('GET',self.base_url,params=payload, headers=self.headers).prepare().url
        response = requests.get(
            self.base_url, params=payload, headers=self.headers).text
        data = json.loads(response)
        results = []
        for movie in data['feed']['movie']:
            title = movie['originalTitle']
            id = movie['code']
            year = movie['productionYear']
            results.append({'id': id, 'title': title, 'year': year})
        return results

    def info(self, id):
        payload = {'partner': 'YW5kcm9pZC12M3M', 'filter': 'movie',
                   'format': 'json', 'code': id, 'scriptags': 'synopsisshort'}
        response = requests.get(
            self.info_url, params=payload, headers=self.headers).text
        data = json.loads(response)
        m = Movie()
        m.id = data['movie']['code']
        m.title = data['movie']['title']
        m.year = data['movie']['productionYear']
        m.plot = data['movie']['synopsisShort']
        return m
