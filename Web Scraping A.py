# Web Scraping

from bs4 import BeautifulSoup
import requests
import random
'''
for i in range(1):
    url = "http://quotes.toscrape.com/page/" + str(i)

    page = requests.get(url)
    # print(page.text)

    soup = BeautifulSoup(page.text, "html.parser")
    #print(soup.prettify())

    # findAll - search by tag name, attribute(kwarg), class(kwarg), string=""
    quotes = soup.findAll("span", class_="text")
    authors = soup.findAll("small", class_="author")
    print(quotes)

    for i in range(len(quotes)):
        print(quotes[i].text)
        print("-", authors[i].text, "\n\n")
'''

url = "https://www.regmovies.com/theaters/regal-webster-place-11/C00129681357"

page = requests.get(url)
#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

titles = [x.text.strip() for x in soup.findAll("h3", class_="title")]
#print(titles)

showtimes = [x.findAll("li", class_="showtime-entry") for x in soup.findAll("div", class_="showtime-panel")]

for i in range(len(titles)):
    print("\n")
    print(titles[i])
    if len(showtimes[i]) > 0:
        for j in range(len(showtimes[i])):
            print(showtimes[i][j].text.strip())
    else:
        print("Coming Soon")



