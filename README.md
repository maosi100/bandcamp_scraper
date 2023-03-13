# Bandcamp scraper and interface

## Project Description
This is a Bandcamp email scraper and visualizer in Python via Flask. 
It automatically scrapes release links from Bandcamp emails after being connected to a valid .mbox file
and runs a Flask application displaying the scrapped releases chronologically within an HTML iframe.

A .mbox export of an email mailbox containing email from Bandcamp must be provided to the application.
The mailbox is automatically scraped of release links and their email timestamp and converted into a
.json file. The .json file is then used by Flask to generate a webapp where each release is displayed.

## Why is this useful?
Bandcamp automatically sends emails for new releases of labels that you follow. But besides release emails
containing the respective links other types of mails containing announcements or messages are sent. Following
many labels on Bandcamp often leads to a cluttered inbox making the process of checking new releases tiresome.

With this app new releases can easily be accessed directly by just refreshing the browser window and having
all revelevant release information containted within an HTML iframe.

## Using the Application
Python 3.11 is required for this application

1. Create a local clone of this github repository:
2. Running the app for the first time a valid .mbox file needs to be provided for execution
    * Create a local export of your Apple Mail Inbox containing the Bandcamp emails
    * Provide the filepath to the .mbox file when running the app: `python main.py ~/.../.../file.mbox` 
3. The databse.json file is accessed to retrieve Bandcamp release links chronologically
4. Flask will run the webapplication on localhost
5. Access each release via the webapplication

* Refresh the page to load the next release
    * A flag is set after viewing each release so each release is only shown once
* You can go back to previously viewed releases using the "Go back one release" button
* If you want to continue browsing forwards you need to press the "Resume Browsing" button once
    * Afterwards refreshing the page works again
* To stop browsing use the "Save and quit" button
    * All flags will be written to the database.json file to remember which releases have been viewed


## Additional Information
To enhance the digging experience I recommend to additionally use
[Bandcamp Enhancement Suite](https://github.com/sabjorn/BandcampEnhancementSuite). 
However to enable this addon within HTML iframes the manifest.json File
needs to include:
```
"content_script": [
    {
        "all_frames": true,
    }
]
```
