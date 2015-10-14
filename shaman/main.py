#!/usr/bin/env python
# -*- coding: utf-8 -*-
# walid.saad

import inquirer
import providers.api as api

from termcolor import colored


class MovieSearch(object):

    def display_results(self, results):
        for index, movie in enumerate(results):
            index = colored(index, 'red', attrs=['blink'])
            title = colored(unicode(movie['title']), 'cyan')
            year = colored(unicode(movie['year']), 'green', attrs=['bold'])
            print u"{} {} {}".format(index, title, year)

    def display_movie(self, movie):
        title = colored(movie.title, 'red', attrs=['blink'])
        year = colored(unicode(movie.year), 'cyan')
        plot = movie.plot
        print u"{} {} \n{}".format(title, year, plot)

    def main(self):
        sites = ['Imdb', 'RottenTomatoes', 'elCinema',
                 "TheMovieDatabase", "Allocine"]
        subs = [
            inquirer.List('site',
                          message="Choose a Provider",
                          choices=sites,
                          ),
        ]
        site = inquirer.prompt(subs)['site'].lower()
        query = raw_input("Search Movie: ")
        results = api.search(query, site)
        movs = dict(enumerate(results))
        self.display_results(results)
        choose = raw_input("pick a movie\t")
        movie = api.info(movs[int(choose)]['id'], site)
        self.display_movie(movie)

if __name__ == '__main__':
    MovieSearch().main()
