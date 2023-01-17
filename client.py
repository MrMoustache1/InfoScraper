from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import datetime
import pandas as pd

def main():
    # URL to scrape ... currently set to the anime season page on MAL
    url_anime = "https://myanimelist.net/anime/season"

    # Open connection, grab page
    uClient = uReq(url_anime)

    # Read page
    page_html = uClient.read()

    # Close connection
    uClient.close()

    # Now we need to parse the HMTL using bs4
    page_soup = soup(page_html, "html.parser")
    print(page_soup)


    # Now we want to traverse the html and find the container objects of each anime... can access each like a py list (indexed)
    containers = page_soup.findAll("div", {"class": "js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1"})

if __name__ == '__main__':
    main()
