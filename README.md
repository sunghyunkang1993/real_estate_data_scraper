# Data scraper

## How to get started
1. spider.py is the main scraper logic
2. spdier.py currently crawl the BiggerPockets forum https://www.biggerpockets.com/forums?page={PAGE_NUMBER}
3. For each post on the forum, it will find post title, author, and topic. Also it will find the user name of the author.
4. it will try to craw the author's profile page

## How to run the scraper
`scrapy crawl bp -o bp.json`
`scrapy crawl bp -o bp.csv`
This will save scraped data in the datastructure that we have determined in the json file `bp.json` or `bp.csv` depending on the chosen format


