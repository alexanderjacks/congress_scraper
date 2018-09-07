# Basic Congress.gov Web Scraper 🐍🇺🇸🤓
## alexanderjacks

## Function
Runs an incognito Chrome browser
+ aimed at this URL: https://www.congress.gov/members?q={%22congress%22:%22115%22}&pageSize=250
+ targets page elements using class names
+ collects text data into 3 arrays (list comprehension)
+ prints data to CLI (aka terminal)
+ matches data across arrays (zip method)

## Install, Run
+ ensure you have virtualenv for your python3
- ```virtualenv -p python3 scrape```
- ```pip install -r setup.py```
- ```python scrape.py```

## Configure...
- which URL of the main 3 you are aiming at; scripts only work on 1 page at a time, congress.gov splits list across 3 URLs

## Use tools to paste into CSV and translate to JSON if desired

## Development Milestones
+ refactor scripts to allow for more features and easy adaptation to other websites
+ build tools to collect and write to JSON file per scrape
