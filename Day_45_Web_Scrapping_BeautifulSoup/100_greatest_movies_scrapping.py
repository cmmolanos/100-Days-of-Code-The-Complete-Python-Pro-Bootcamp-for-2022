import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
movies_html = requests.get(URL).text

soup = BeautifulSoup(movies_html, "html.parser")

#movies = soup.find_all(class_="article-title-description__text")

movies = soup.select(".article-title-description h3.title")
movies_titles = [m.text for m in movies]
movies_titles.reverse()

with open("movies.txt", "w") as file:
    for movie in movies_titles:
        file.write(f"{movie}\n")
