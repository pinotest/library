#from faker import Faker
from datetime import datetime
from BaseMovie import BaseMovie
from SeriesMovie import SeriesMovie

#fake = Faker('pl_PL')

library = []

def get_movies(library):
    '''
    Function gets two arguments: 
    card type 0 - create businessContact or other - create BaseContact
    amount - number of cards to create
    and return a list of created cards
    '''
    library_movies = []
    for i,j in enumerate(library):
        if (type(library[i])==BaseMovie):
            library_movies.append(library[i])
    return sorted(library_movies, key=lambda Movie: Movie.title)
    #if card_type == 0:
    #    return [BusinessContact(fake.company(), fake.job(), fake.phone_number(),fake.first_name(),fake.last_name(), 
    #    fake.phone_number(), fake.email()) for i in range(amount)]
    #return [BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()) for i in range(amount)]

def get_series(library):
    library_series = []
    for i,j in enumerate(library):
        if (type(library[i])==SeriesMovie):
            library_series.append(library[i])
    return sorted(library_series, key=lambda Movie: Movie.title)
    #Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.

def search(title):
#    Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
    library_search = []
    for i,j in enumerate(library):
        if (library[i].title.upper() == title.upper()):
            library_search.append(library[i])
    return sorted(library_search, key=lambda Movie: Movie.title)

def generate_views():
    #Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
    pass

def generate_views_times(how_many_times):
    #Napisz funkcję, która uruchomi generate_views 10 razy.
    pass

def top_titles(content_type):
    #Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. 
    #Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
    pass

#dla chętnych
#Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. 
#Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.
def add_full_season_series(title, initial_release, content_type, season_number, episode_numbers):
    for i in range(1, episode_numbers+1):
        library.append (SeriesMovie(title=title,initial_release=initial_release,content_type=content_type,season_number=season_number, episode_number=i))

#Niech program po uruchomieniu działa w następujący sposób:
#Wyświetli na konsoli komunikat Biblioteka filmów.
#Wypełni bibliotekę treścią.
#Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
#Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
#Wyświetli listę top 3 najpopularniejszych tytułów.

print("=== Biblioteka filmów ====")
add_full_season_series("Friends", 1994, "comedy", 1, 2)
add_full_season_series("Game of Thrones", 2011, "drama", 10, 2)
add_full_season_series("Alien", 1991, "horror", 1, 2)
library.append(BaseMovie("Truman Show", 1999, ""))

#print(get_series(library))
#print(search("game of thrones"))

