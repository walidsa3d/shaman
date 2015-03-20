import inquirer
from termcolor import colored
from providers.imdb import imdby as Imdb
import providers.elcinema as elcinema
class MovieSearch:  
   
    def display_results(self, results):
        for index,movie in enumerate(results):
            index=colored(index,'red',attrs=['blink'])
            title=colored(unicode(movie['title']),'cyan')
            year=colored(unicode(movie['year']),'green',attrs=['bold'])
            print index+" "+title+" "+year

    def display_movie(self,movie):
        title=colored(movie.title,'red',attrs=['blink'])
        year=colored(unicode(movie.year),'cyan')
        plot=movie.plot
        print title+" "+year+"\n"
        print plot

    def main(self):
        sites=['Imdb','RottenTomatoes','elCinema']
        subs = [
              inquirer.List('site',
                            message="Choose a Provider",
                            choices=sites,
                        ),
            ]
        site = inquirer.prompt(subs)['site'].lower()
        query=raw_input("Search Movie: ")
        if(site=="imdb"):
            results=Imdb().search(query)
        if(site=="elcinema"):
            results=elcinema.search(query)
        movs=dict(enumerate(results))
        self.display_results(results)
        choose=raw_input("choose movie\t")
        print movs[int(choose)]
        movie=elcinema.get_details(movs[int(choose)]['id'])
        self.display_movie(movie)

if __name__ == '__main__':
    MovieSearch().main()