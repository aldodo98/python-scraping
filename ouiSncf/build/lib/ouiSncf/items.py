# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OuisncfItem(scrapy.Item):
    # define the fields for your item here like:
    title_activity = scrapy.Field()
    url_activity = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()

