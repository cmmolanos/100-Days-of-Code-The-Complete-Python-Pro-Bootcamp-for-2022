from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

titles = soup.find_all(name="a", class_="titlelink")
tags = [t.text for t in titles]

links = [t.get("href") for t in titles]

scores = soup.find_all(class_="score")
scores = [int(s.text.split(' ')[0]) for s in scores]

max_score_index = scores.index(max(scores))

print("The most rated article now")
print("\t", tags[max_score_index], links[max_score_index])