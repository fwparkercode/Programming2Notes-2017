from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # uniform resource locator

page = requests.get(url)  # get request to the website url

#print(page.text)

# make a bs object to scrape, Beautiful Soup parses the page
soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

# find data/text using findAll function
# findAll can search by tagname, attributes(kwargs), css class(kwarg), or string

# by tagname
title = soup.findAll("title")
print(title)

# by attribute
header = soup.findAll(style="text-decoration: none")
print(header)

# by css class
tags = soup.findAll(class_="tags")
print(tags)

# by string
einstein = soup.findAll(string="Albert Einstein")
print(einstein)

# any combination of above
# find all quotes
quotes = soup.findAll("span", class_="text")



# find all authors
authors = soup.findAll("small", class_="author")


for i in range(len(quotes)):
    print(quotes[i].text)
    print("-", authors[i].text, "\n")



# Regal Webster Scrape
url = "https://www.regmovies.com/theaters/regal-webster-place-11/C00129681357"

page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

titles = soup.findAll("h3", class_="title")

titles = [x.text.strip() for x in titles]
print(titles)

movie_times = soup.findAll("ul", class_="format-showtimes")
print(movie_times[0])

show_times = []
for times in movie_times:
    show_time = times.findAll("li", class_="showtime-entry")
    show_times.append(show_time)

print(show_times)

for i in range(11):
    print("\n")
    print(titles[i])
    for time in show_times[i]:
        print(time.text.strip())





