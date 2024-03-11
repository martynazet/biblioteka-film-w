# biblioteka filmów
import random
import datetime

class Movies:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1
        return f'Current views: {self.views}'
    
    def views(self):
        return self.views

    def __str__(self):
        return f'{self.title} ({self.year})'
    
    def __repr__(self):
        return f'{self.title} ({self.year})'

class Series(Movies):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d} ({self.year})"
    
    def __repr__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"



def get_movies(random_library):
    movies = []
    for i in random_library:
        if type(i) is Movies:
            movies.append(i)
    sorted_movies = sorted(movies, key=lambda movie: movie.title)
    return sorted_movies
    

def get_series(random_library):
    series = []
    for i in random_library:
        if type(i) is Series:
            series.append(i)
    sorted_series = sorted(series, key=lambda serial: serial.title)
    return sorted_series

        
def search(title, random_lib):
    searching_list = [x for x in random_lib if title in x.title]
    if not searching_list:
        print(f"There is no {title} in library")
    else:
        print(searching_list)

def generate_views(random_lib):
    selected_item = random.choice(random_lib)
    selected_item.views += random.randint(1, 100)
    #print(f'{selected_item} Current views: {selected_item.views}')

def more_views(random_lib):
    for _ in range(10):
        generate_views(random_lib)

def top_titles(how_many, random_lib, content_type):
    movies = []
    series = []
    for i in random_lib:
        if type(i) is Movies:
            movies.append(i)
        elif type(i) is Series:
            series.append(i)
    movies_sorted = sorted(movies, key=lambda x: x.views, reverse=True)
    series_sorted = sorted(series, key=lambda x: x.views, reverse=True)
    top_movies = movies_sorted[0:how_many]
    top_series = series_sorted[0:how_many]

    if content_type == 'movies':
        print(top_movies)
    elif content_type == 'series':
        print(top_series)
    else:
        print("Wrong content")
    

def add_season(random_lib, ep_title, ep_season, eps_number, ep_year, ep_genre):
    for i in range(1, eps_number + 1):
        episode = Series(title = ep_title, year = ep_year, season = ep_season, episode = i, genre = ep_genre)
        random_lib.append(episode)



if __name__ == '__main__':
    print('----- MOVIE LIBRARY -----')

    movie1 = Movies(title='Pulp Fiction', year='1994', genre='action')
    movie2 = Movies(title='Interstellar', year='2014', genre='sci-fi')
    movie3 = Movies(title='Gladiator', year='2000', genre='drama')
    movie4 = Movies(title='Barbie', year='2023', genre='comedy')
    series1 = Series(title='Friends', year='1994', genre='comedy', season =5, episode=5)
    series2 = Series(title='For All Mankind', year='2022', genre='sci-fi', season=1, episode=3)
    series3 = Series(title='Friends', year='1994', genre='comedy', season =6, episode=2)
    series4 = Series(title='Brooklyn 9-9', year='2013', genre='comedy', season =2, episode=1)
    
    library = [movie1, movie2, movie3, movie4, series1, series2, series3, series4]
    add_season(library, 'The Office', 1, 24, '2005', 'comedy')
    more_views(library)
    today = datetime.date.today()
    print(f'Top movies from day {today}:') 
    top_titles(3, library, 'movies')
    print(f'Top series from day {today}:')
    top_titles(3, library, 'series')
    
