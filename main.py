from datetime import datetime
from BaseMovie import BaseMovie
from SeriesMovie import SeriesMovie
import random

library = []

def get_movies():
    '''
    Function returns sorted list of movies from library list without tv series
    '''
    library_movies = [j for i,j in enumerate(library) if (type(library[i])==BaseMovie) ]
    return sorted(library_movies, key=lambda Movie: Movie.title)

def get_series():
    '''
    Function returns sorted list of TV series from library list without movies
    '''
    library_series = [j for i,j in enumerate(library) if (type(library[i])==SeriesMovie)]
    return sorted(library_series, key=lambda Movie: Movie.title)
 
def search(title):
    '''
    Function return sorted list of movies or tv series title from library for a given argument title  
    '''
    library_search = [j for i,j in enumerate(library) if (library[i].title.upper() == title.upper())]
    return sorted(library_search, key=lambda Movie: Movie.title)

def generate_views():
    '''
    Function choose random element of library, generate random number of plays and  execute function play()  
    '''
    drawn_movie = random.randint(0,len(library)-1)
    how_many_times = random.randint(1,100) 
    for i in range(how_many_times):
        library[drawn_movie].play()

def generate_views_ten_times():
    '''
    Function only execute 10 times function generate_views()
    '''
    for i in range(10):
        generate_views()

def top_titles(top_number, content_type=2):
    '''
    Function gets two arguments:
    - top_number - number of element that should be return
    - content_type with default value = 2, used to filtr a library before selecting top_number, 
    Content_type: 0 - Movies, 1 - TV Series, Other - Movies and TV series
    Returns a list with top_number of selected movies from library with the highest value of number_plays
    '''
    if content_type == 0:
        temp_library = get_movies()
        print("Najpopularniejsze filmy dnia ", datetime.strftime(datetime.now(),'%d:%m:%Y'))
    elif content_type == 1:
        print("Najpopularniejsze seriale dnia ", datetime.strftime(datetime.now(),'%d:%m:%Y'))
        temp_library = get_series()
    else:
        temp_library = library
        print("Najpopularniejsze filmy i seriale dnia ", datetime.strftime(datetime.now(),'%d:%m:%Y'))

    sorted_library = sorted(temp_library, key=lambda Movie: Movie.number_plays, reverse=True)
    top_library = []
    for i in range(top_number):
        top_library.append(sorted_library[i])
    return top_library

def add_full_season_series(title, initial_release, content_type, season_number, episode_numbers):
    '''
    Function gets arguments to create SeriesMovie objects and add them to library for each eposide_number
    '''    
    for i in range(1, episode_numbers+1):
        library.append (SeriesMovie(title=title,initial_release=initial_release,content_type=content_type,season_number=season_number, episode_number=i))

def number_of_episodes(title, season=1):
    '''
    Function gets title and season argument (default 1) and return for a given title and season number of episodes
    '''
    library = search(title)
    episode_count = 0
    for i,j in enumerate(library):
        if library[i].season_number == season:
            episode_count += 1
    return episode_count

print("=== Biblioteka filmów ====")
print("Dodaję seriale i filmy...")
add_full_season_series("Friends", 1994, "comedy", 1, 19)
add_full_season_series("Friends", 1995, "comedy", 2, 20)
add_full_season_series("Friends", 1996, "comedy", 3, 21)
add_full_season_series("Game of Thrones", 2011, "drama", 10, 8)
add_full_season_series("Aliens", 1991, "horror", 1, 9)
add_full_season_series("Lost", 2004, "drama", 1, 22)
add_full_season_series("Lost", 2005, "drama", 2, 20)
library.append(BaseMovie("Truman Show", 1999, "comedy"))
library.append(BaseMovie("Upgrade", 2018, "sci-fi"))
library.append(BaseMovie("Alien", 1979, "horror"))
library.append(BaseMovie("The shining", 1980, "horror"))
print("Generuję dla losowych pozycji ilość wypożyczeń...")
generate_views_ten_times()
generate_views_ten_times()
generate_views_ten_times()
print("---------")
print(top_titles(3,0))
print("---------")
print(top_titles(3,1))
print("---------")

top_movies = top_titles(3) 
for i,j in enumerate(top_movies):
    print(top_movies[i].title, top_movies[i].number_plays)

print("---------")
print("Liczba odcinków Lost w sezonie 2: ", number_of_episodes("Lost",2))
print("Liczba odcinków Friends w sezonie 1: ", number_of_episodes("Friends"))



