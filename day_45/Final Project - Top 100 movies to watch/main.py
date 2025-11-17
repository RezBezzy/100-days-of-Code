import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#print(soup)

movies = soup.find_all(name="h3")
#print(movies)

movie_texts = []

for movie in movies:
    movie_text = movie.getText()
    movie_texts.append(movie_text)

movies_texts_reversed = movie_texts[::-1]

# movie_texts_sort = sorted(movie_texts)
# print(movie_texts_sort)

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_texts_reversed:
        file.write(movie + "\n")