> # Jan 16, 2023
> ### Changelog
> * Created empty website
> * Created working web scraper. Can scrape [Seasonal Mal Page](https://myanimelist.net/anime/season) (currently only for one anime) and retrieve the anime title, and rating.
>
> ### Bug list
> The following are all bugs found in the web scraper:
> - [ ] Anime rating sometimes doesn't match anime title
> - [ ] Anime original release date sometimes doesn't match anime title
> - [ ] "Invalid input" for some anime
> - [x] CSV isn't being written properly. Only the header for the CSV is being written
>
> ### To-do list
> - [ ] Fix bugs
> - [ ] Add more functionality to website
> - [ ] Loop the scraper actions so it can scrape info for all anime on the page
>   * make sure to keep in mind dealing with ratings of "N/A" and characters that cannot be encoded (?)
> - [ ] Add more functionality to the scraper (scrape more info for anime)