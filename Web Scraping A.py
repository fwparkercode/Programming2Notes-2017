# Web Scraping

from bs4 import BeautifulSoup
import requests
import random

for i in range(1, 11):
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

