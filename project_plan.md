# Bancamp Email Interface 

## Solving which Problem?

* Having to go through all bandcamp emails to get to the release mails
* Having to click every release link from Bandcamp emails individually
* Having to load each page of the release
* Having to delelte the bandcamp mail individually after checking the release

## Main tasks

1. Access the currently existing Bandcamp emails in Bandcamp folder
2. Scrape through X Emails until Y release links have been found
3. Generate an Application Interface based on these Y release links
    * Generate a "tab" for every release link
    * First open tab includes the relase items (tracks)
    * A possibility to listen to the items (player)
    * A buy button that forwards to the bandcamp page of the track
    * Closing the tab and deleting the associated email in the folder
    * Automatically jumping to the next tab
    * Automatically loading the next release link to a total of Y active links

## Project Strucutre

### Main Applications and features

1. Email Scraper
    * Searches through the emails and extracts the requiered links
    * Search through an offline mailbox in .mbox format
2. Web Scraper
    * Uses links from the Email Scraper to access the release
    * Scrapes the following data:
        * Release Name and Artist
        * Release Date
        * Release Cover
        * Label and label Art
        * The individual tracks
        * The link to buy the individual tracks
3. Scraper Interface
    * Creates a visual interface using Webscraper data
    * One tab per release
    * Contains the bandcamp player and waveform
    * Let's you access each individual tracks buy link
    * Closing the tab deletes the associated email

### Data Flow

```
* Email Scraper -> Webscraper (Link data)
* Web scraper -> Scraper Interface (Release data)
* Scraper Interface -> ??? (Delete Email)
```
