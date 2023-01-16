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

    # Now we want to traverse the html and find the container objects of each anime... can access each like a py list (indexed)
    containers = page_soup.findAll("div", {"class": "js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1"})

    """
    #[DEBUGGING] 
    #Checking number of containers
    print(len(containers))
    """

    # Making csv file
    filename = "CSV_Database.csv"
    f = open(filename, "w")
    headers = "anime_name, rating, release_schedule\n"
    f.write(headers)

    months_dict = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    days_dict = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # Loop getting anime titles from all containers
    for i in range(len(containers)):
        try:
            ani_title = ((str(containers[i].div.h2.a).removeprefix('<')).partition('>')[2]).removesuffix('</a>')

        # Gets anime title
            ani_rating = str(page_soup.findAll("span", {"class": "js-score"})[i]).removesuffix('<').partition('none;">')[2].removesuffix('</span>')
            if ani_rating == "N/A":
                print('An invalid entry has been skipped\n\n')

        # Loop getting anime release date schedule.
        # #!!!!! Can make this much more efficient indexing through objects in tag
        # !!!!!! BUGGGG: line 65 first index: [0] ??? Leap Years??? Straight up some wrong values 
            ani_release_date = str(page_soup.findAll("div", {"class": "info"})[i]).removeprefix('<').partition('"item">')[2]
            ani_release_date = ani_release_date.split('<', 1)[0].replace(',', '').split(' ')
            ani_release_sched = datetime.date(int(ani_release_date[2]), int(ani_release_date[1]), months_dict[ani_release_date[0]])
            #[DEBUGGING] print("datetime: ", ani_release_sched)
            ani_release_sched = int(ani_release_sched.weekday())
            ani_release_sched = (ani_release_sched + 2) % 7
            ani_release_sched = days_dict[ani_release_sched]

            print("Title: ", ani_title)
            print("Rating: ", ani_rating)
            print("Release date: ", ani_release_date)
            print("Release sched: ", ani_release_sched)
            print("\n\n")

        # Formatting release date so it doesnt make extra columns on csv file
            ani_release_date = str(ani_release_date.remove(','))

        # Writing data into csv file
            f.write(str(ani_title.replace(',', ' ')) + "," + str(ani_rating) + "," + ani_release_date + "," + str(ani_release_sched) + "\n")

        except(UnicodeEncodeError and ValueError):
            print('An invalid entry has been skipped\n\n')
            continue

    # Closing csv file
    f.close()

if __name__ == '__main__':
    main()