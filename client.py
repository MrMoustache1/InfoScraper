from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from csv import DictWriter
import datetime
import pandas as pd
import csv_writer


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

    # Now we want to traverse the html and find the container objects of each anime... can access each like a py list (indexed)
    containers = page_soup.findAll(
        "div",
        {
            "class": "js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1"
        },
    )

    # Looping for every anime container on that page
    for i in range(len(containers)):
        try:
            # Getting anime title
            ani_title = str(containers[i].h2)
            ani_title = ani_title.split(">")[2].split("<")[0]
            print("\n\n")
            print(ani_title)

            # Getting anime rating
            ani_score = str(containers[i])
            ani_score = str(page_soup.findAll("div", {"title": "Score"})[i])
            ani_score = ani_score.split(">", 2)[2].split(">")[1].split()[0]
            print(ani_score)

            # Calling csv_create_and_fill func from ./csv_writer.py file
            csv_writer.csv_create_and_fill(ani_title, ani_score)

        # Error handling. There are some anime titles with invalid unicode chars
        except (UnicodeEncodeError):
            print("Encountered Unicode Encode Error for an anime title")
            continue


if __name__ == "__main__":
    main()
