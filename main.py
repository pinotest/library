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
    drawn_movie = random.randint(0,len(library)-1)
    how_many_times = random.randint(1,100) 
    for i in range(how_many_times):
        library[drawn_movie].play()

def generate_views_ten_times():
    #Napisz funkcję, która uruchomi generate_views 10 razy.
    for i in range(10):
        generate_views()

def top_titles(content_type):
    #Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. 
    #Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
    '''
    Content_typ: 0 - Movies, 1 - TV Series, Other - Movies and TV series
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

#dla chętnych
#Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. 
#Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.
def add_full_season_series(title, initial_release, content_type, season_number, episode_numbers):
    for i in range(1, episode_numbers+1):
        library.append (SeriesMovie(title=title,initial_release=initial_release,content_type=content_type,season_number=season_number, episode_number=i))
        
def number_of_episodes(title, season=1):
    library = search(title)
    episode_count = 0
    for i,j in enumerate(library):
        if library[i].season_number == season:
            episode_count += 1
    return episode_count
        
#Niech program po uruchomieniu działa w następujący sposób:
#Wyświetli na konsoli komunikat Biblioteka filmów.
print("=== Biblioteka filmów ====")
#Wypełni bibliotekę treścią.
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
#Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
generate_views_ten_times()
generate_views_ten_times()
generate_views_ten_times()
#Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
#Wyświetli listę top 3 najpopularniejszych tytułów.
#top filmy
print(top_titles(3,0))
#top seriale
print(top_titles(3,1))
#top filmy i seriale
print(top_titles(3))

print("---------")
print("Liczba odcinków Lost w sezonie 2: ", number_of_episodes("Lost",2))

