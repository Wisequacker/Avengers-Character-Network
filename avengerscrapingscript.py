import pandas as pd
import requests
from bs4 import BeautifulSoup

## this is the list of films of interest
## everything fandom movie is migrating to movie fandom, so there isn't currently a scrapable transcript is NOT available
url_list = ["Avengers:_Infinity_War/Transcript", "Avengers:_Endgame/Transcript",
    "Avengers:_Age_of_Ultron/Transcript", "Captain_America:_Civil_War/Transcript"]
title_list = ["Avengers_Infinity_War","Avengers_Endgame","Avengers_Age_of_Ultron","Captain_America_Civil_War"]

## script that scrapes the necessary collection of tabs in the
for url in url_list:
    for title in title_list:
        response = requests.get("https://movies.fandom.com/wiki/" + url)
        html_string = response.text
        document = BeautifulSoup(html_string, "html.parser")
        script_div = document.find_all("div", {"class": "mw-parser-output"})
        ## make the result set output into a str that can be written into a text file
        string = str(script_div)
        open('{film_title}.txt'.format(film_title=title), mode='w', encoding='utf-8').write(string)

## Post script scraping processing is necessary to remove all the irrelevant tags and add back contractions
