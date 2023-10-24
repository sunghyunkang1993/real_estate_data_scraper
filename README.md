# Data scraper

## How to get started
1. spider.py is the main scraper logic
2. spdier.py currently crawl the BiggerPockets forum https://www.biggerpockets.com/forums?page={PAGE_NUMBER}
3. For each post on the forum, it will find post title, author, and topic. Also it will find the user name of the author.
4. it will try to craw the author's profile page

## Moifications
1. Crawl the forum page and find the href link
2. Crawl the actual post page that has comments from the href from 1


