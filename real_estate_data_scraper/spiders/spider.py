import scrapy
from scrapy.http.response import Response

class BPSpider(scrapy.Spider):
    name = "bp"

    def start_requests(self):
        urls = [
            "https://www.biggerpockets.com/forums?page=1"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response):
        posts = response.xpath('//div[contains(@class, "simplified-forums__card-wrapper-compact")]')
        for post in posts:
            post_title = post.xpath('.//div[contains(@class, "simplified-forums__card-header-compact")]//a/text()').get()
            author = post.xpath('.//a[contains(@class, "simplified-forums__user__profile-link")]/text()').get()
            topic = post.xpath('.//a[contains(@class, "simplified-forums__topic-metadata__link")]/text()').get()
            profile_link = post.xpath('.//a[contains(@class, "simplified-forums__user__profile-link")]//@href').get()
            user_profile_link = "https://www.biggerpockets.com" + profile_link
            yield scrapy.Request(user_profile_link, callback=self.parse_user)


    def parse_user(self, response: Response):
        ### 403 ERROR for SCRAPE
        print(response.xpath('//div[contains(@class, "user-about-me")]//p').getall())
