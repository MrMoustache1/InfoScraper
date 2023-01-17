from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#import csv
from csv import DictWriter
import datetime
import pandas as pd
import header_csv

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
    #print(page_soup)

    # Making CSV File
    #filename = "CSV_Database.csv"
    #f = open(filename, "w")
    #headers = "anime_name, rating"
    #f.write(headers)

    # HAVE TO WRITE ONE ARGUMENT AT A TIME, SO FORMAT IT
    #data = ani_title.replace(',', ' ') + "," + ani_score
    #list_of_data = [ani_title, ani_score]
    #field_names = ["anime_name", "rating"]
    #field_names = "anime_name, rating"
    #list_of_ani_titles = []
    #list_of_ani_ratings = []
    #dict = {}


    # Now we want to traverse the html and find the container objects of each anime... can access each like a py list (indexed)
    containers = page_soup.findAll("div", {"class": "js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1"})
    print(containers[0])

    # Getting anime title
    ani_title = str(containers[0].h2)
    ani_title = ani_title.split(">")[2].split("<")[0]
    print("\n\n")
    print(ani_title)
    #list_of_ani_titles.append(ani_title)
    #dict["anime_name"] = ani_title


    # Getting anime rating
    ani_score = str(containers[0])
    ani_score = str(page_soup.findAll("div", {"title": "Score"})[0])
    ani_score = ani_score.split(">", 2)[2].split(">")[1].split()[0]
    print(ani_score)
    print("\n\n")
    #list_of_ani_ratings.append(ani_score)
    #dict["rating"] = ani_score

    #print(list_of_ani_ratings)
    #print(list_of_ani_titles)
    # Get writer object
    #writer_object = writer(f)

    # Putting info in CSV file
    #f.write(list_of_data)
    #writer_object.writerow(list_of_data)

    # CSV connection with header file
    header_csv.csv_create_and_fill(ani_title, ani_score)

"""    with open('CSV_Database.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames = field_names)
        dictwriter_object.writerow(dict)
        # Close CSV file
        f_object.close()"""

if __name__ == '__main__':
    main()
