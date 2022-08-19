import scrapy
from scrapy.http.headers import Headers
import json
import random
class CalendrierSpider(scrapy.Spider):
    name = 'calendrier'
    allowed_domains = ['www.sncf-connect.com']
    start_urls = ['https://www.sncf-connect.com/app/home/shop/results/outward']

    def parse(self, response):
        pass
