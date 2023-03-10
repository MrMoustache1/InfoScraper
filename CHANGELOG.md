# Feb 13, 2023 
> ### Changelog
> * Added React functionality into site.
> * Merged all branches into Main
> * Organized most project required files and folders
> * Added 'How to Run' section to the README
> ### Bug list
> * Check Jan 16 to-do
> ### To-do list
> - Basic website funtionality
> - API integration
> - Integrating the scraper into the JS

# Jan 27, 2023
> ### Changelog
> * Fixed most bugs in the scrapper (removed any dating functionality in scrapper)
> * PR to merge scraper-debugging to scraper branch
> ### Bug list
> * None found in scrapper
> ### To-do list
> - Refer to Jan 16 to-do

> # Jan 16, 2023
> ### Changelog
> * Created empty website
> * Created working web scraper. Can scrape [Seasonal Mal Page](https://myanimelist.net/anime/season) (currently only for one anime) and retrieve the anime title, and rating.
>
> ### Bug list
> The following are all bugs found in the web scraper:
> - [x] Anime rating sometimes doesn't match anime title
> - [ ] Anime original release date sometimes doesn't match anime title
> - [x] "Invalid input" for some anime
> - [x] CSV isn't being written properly. Only the header for the CSV is being written
>
> ### To-do list
> - [x] Fix bugs
> - [ ] Add more functionality to website
> - [x] Loop the scraper actions so it can scrape info for all anime on the page
>   * make sure to keep in mind dealing with ratings of "N/A" and characters that cannot be encoded (?)
> - [ ] Add more functionality to the scraper (scrape more info for anime)