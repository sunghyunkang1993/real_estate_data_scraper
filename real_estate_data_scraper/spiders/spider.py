import scrapy
from scrapy.http.response import Response


class BPSpider(scrapy.Spider):
  name = "bp"
  print("This statement runs in the BPSpider constructor")

  def start_requests(self):
    urls = ["https://www.biggerpockets.com/forums?page=1"]

    # We want to be able to search and scrape for specific search terms like theses
    # urls = [
    #     "https://www.biggerpockets.com/search/topics?term=indianapolis+cash+flow",
    #     "https://www.biggerpockets.com/search/topics?term=interest+rate+adjustments"
    # ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response: Response):
    print("This statement runs at the beginning of the parse function")

    PostDict = {
        0: [
            "ExampleTitle", "ExampleURL", "ExampleAuthor", "ExampleTopic",
            "ExampleProfLink", "ExampleUserProfLink", "ExamplePostURLLink"
        ]
    }
    # title, url, author, topic, profile_link, user_profile_link, post_url_link,

    posts = response.xpath(
        '//div[contains(@class, "simplified-forums__card-wrapper-compact")]')
    i = 0
    for post in posts:
      i += 1
      post_title = post.xpath(
          './/div[contains(@class, "simplified-forums__card-header-compact")]//a/text()'
      ).get()
      post_url = post.xpath(
          './/h2[contains(@class, "simplified-forums__topic-content__title")]//a//@href'
      ).get()
      author = post.xpath(
          './/a[contains(@class, "simplified-forums__user__profile-link")]/text()'
      ).get()
      topic = post.xpath(
          './/a[contains(@class, "simplified-forums__topic-metadata__link")]/text()'
      ).get()
      profile_link = post.xpath(
          './/a[contains(@class, "simplified-forums__user__profile-link")]//@href'
      ).get()

      print("This is the post URL if it was retrieved: " + post_url)
      user_profile_link = "https://www.biggerpockets.com" + profile_link
      post_url_link = "https://www.biggerpockets.com" + post_url
      yield scrapy.Request(post_url_link, callback=self.parse_post)

      PostDict[i] = [
          post_title, post_url, author, topic, profile_link, user_profile_link,
          post_url_link
      ]
      print(post_title, author, topic, profile_link, user_profile_link)

    print("Here's the dict of posts: ", PostDict)

  def parse_post(self, response: Response):
    ### 403 ERROR for SCRAPE
    print(
        response.xpath(
            '//div[contains(@class, "simplified-forums__topic-content__body-container")]//p'
        ).getall())


# BPScrapeInstance = BPSpider(name="bp")
# BPScrapeInstance.start_requests()
# BPScrapeInstance.parse(BPScrapeInstance.start_requests())

print("This statement prints after instance runs")
