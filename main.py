from bs4 import BeautifulSoup
import requests
import lxml

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
reqs = requests.get(url).text

soup = BeautifulSoup(reqs, "lxml")
urls = []

all_movies = soup.find_all(name="h3", class_="title")

movie_list = [movie.getText() for movie in all_movies]

for movie in range(len(movie_list) -1,-1,-1):
    print(movie_list[movie])