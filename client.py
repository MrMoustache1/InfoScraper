from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

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
# Checking number of containers
print(len(containers))
"""

# Loop getting anime titles from all containers
#for container in containers:
ani_title = ((str(containers[0].div.h2.a).removeprefix('<')).partition('>')[2]).removesuffix('</a>') # Gets anime title

# Loop getting anime rating
#for container in containers:
ani_rating = str(page_soup.findAll("span", {"class": "js-score"})[0]).removesuffix('<').partition('none;">')[2].removesuffix('</span>')

"""
# Check container info
print(ani_title)
print(ani_rating)
"""