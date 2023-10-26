import scrapy
from scrapy.http.response import Response
import json


class BPSpider(scrapy.Spider):
  name = "bp"
  print("This statement runs in the BPSpider constructor")

  def __init__(self):
    self.post_data = []

  def start_requests(self):
    urls = ["https://www.biggerpockets.com/forums?page=1", "https://www.biggerpockets.com/forums?page=2", "https://www.biggerpockets.com/forums?page=3", "https://www.biggerpockets.com/forums?page=4", "https://www.biggerpockets.com/forums?page=5"]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response: Response):
    posts = response.xpath(
        '//div[contains(@class, "simplified-forums__card-wrapper-compact")]')

    for index in range(len(posts)):
      post = posts[index]
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

      user_profile_link = "https://www.biggerpockets.com" + profile_link
      post_url_link = "https://www.biggerpockets.com" + post_url
      
      post_dict = {
        "post_title": post_title,
        "post_url": post_url_link,
        "author": author,
        "topic": topic,
        "profile_link": user_profile_link
      }
      yield scrapy.Request(post_url_link, callback=self.parse_post, cb_kwargs=dict(post_dict=post_dict))

  def parse_post(self, response: Response, post_dict):
    ### 403 ERROR for SCRAPE
    initial_post = response.xpath(
        '//div[contains(@class, "simplified-forums__topic-content__body-container")]//p'
    ).getall()
    post_dict["initial_post"] = initial_post
    yield post_dict
