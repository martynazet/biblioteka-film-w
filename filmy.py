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



def top_titles(how_many, random_lib, content_type):
    content = []
    for i in random_lib:
        if content_type == Movies or content_type == Series:
            content.append(i)
    if content:
        content_sorted = sorted(content, key=lambda x: x.views, reverse=True)
        top_titles = content_sorted[:how_many]
        print(top_titles)
    else:
        print("Wrong content")

      
def get_movies(random_library, how_many):
    return top_titles(how_many, random_library, Movies)

def get_series(random_library, how_many):
    return top_titles(how_many, random_library, Series)
        
def search(title, random_lib):
    for i in random_lib:
        if title == i.title:
            print(f"There is {title} in library.")
            break
    else:
        print(f"There is no {title} in library.")
            
            
def generate_views(random_lib):
    selected_item = random.choice(random_lib)
    selected_item.views += random.randint(1, 100)
    #print(f'{selected_item} Current views: {selected_item.views}')

def more_views(random_lib):
    for _ in range(10):
        generate_views(random_lib)

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
    get_movies(library, 3)
    print(f'Top series from day {today}:')
    get_series(library, 2)
    search("Interstellar", library)
    
    
