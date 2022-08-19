import scrapy
import datetime
from scrapy.http import Request
from itemloaders.processors import MapCompose, Join
from numpy.core import unicode
from ouiSncf.items import OuisncfItem
from scrapy.loader import ItemLoader
class MainsiteSpider(scrapy.Spider):
    name = 'mainSite'
    allowed_domains = ['https://www.coltortiboutique.com/']
    start_urls = ['https://www.coltortiboutique.com/en_eu/women.html']

    def parse(self, response):
        """
                @url http://www.sncf-connect.com/
                @returns items 1
                @scrapes title_activity
                @scrapes url
        """
        tex = OuisncfItem()
        if response.status == 200:
            title = response.xpath('//*[@class="vsc-body-1 vsc-card-product__title"][1]/text()').extract()
            num_it = 0
            for i in title:
                num_it+=1
                path_activity = '//*[@id="ad-mea-'+str(num_it)+'"]//a/@href'
                path_image = '//*[@id="ad-mea-'+str(num_it)+'"]//img/@data-src'
                l = ItemLoader(item=OuisncfItem(), response=response)
                l.add_value('title_activity', i,MapCompose(lambda i:i.replace('\n', ''),unicode.strip))
                l.add_value('url', 'www.sncf-connect.com')
                l.add_xpath('url_activity',path_activity,MapCompose(lambda i:'http://www.sncf-connect.com'+i))
                l.add_xpath('image_urls', path_image, MapCompose(lambda i: 'http://www.sncf-connect.com' + i))

                ll=l.load_item()
                yield ll



