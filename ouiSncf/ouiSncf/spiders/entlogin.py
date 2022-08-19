import scrapy
from scrapy.http import FormRequest
from ouiSncf.items import OuisncfItem
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Join


class EntloginSpider(scrapy.Spider):
    name = 'entlogin'
    allowed_domains = ['ent.uca.fr']
    # start_urls = ['https://ent.uca.fr/core/home']
    def start_requests(self):
        return[
            FormRequest(
                "https://ent.uca.fr/cas/login",
                formdata={"username": "zhxu10", "password": "doss820pc@"}
            )]

    def parse(self, response):
        print(response.xpath('/html/body/div[4]/div[1]/h2/text()'))
