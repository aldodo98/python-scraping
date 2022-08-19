import scrapy
from itemloaders.processors import MapCompose
from numpy.core import unicode
from ouiSncf.items import OuisncfItem
from scrapy.loader import ItemLoader

class MainsiteSpider(scrapy.Spider):
    name = 'mainSite'
    start_urls = ['https://www.sncf-connect.com/']

    def parse(self, response):
        """
                @url http://www.sncf-connect.com/
                @returns items 1
                @scrapes title_activity
                @scrapes url
        """
        if response.status == 200:

            title = response.xpath('//*[@id="block1_miseenavant"]/div/ul/li/div[1]/div/div/div[1]/p[1]/text()')
            num_it = 0
            for i in title:
                num_it+=1
                path_activity = '//*[@id="ad-mea-'+str(num_it)+'"]//a/@href'
                path_image = '//*[@id="ad-mea-'+str(num_it)+'"]//img/@data-src'
                l = ItemLoader(item=OuisncfItem(), response=response)
                # l.add_value('title_activity', i,MapCompose(lambda i:i.replace('\n', ''),unicode.strip))
                l.add_value('title_activity',i.extract(),MapCompose(lambda i:i.replace('\n', ''),unicode.strip))
                l.add_value('url', 'www.sncf-connect.com')
                l.add_xpath('url_activity',path_activity,MapCompose(lambda i:'http://www.sncf-connect.com'+i))
                l.add_xpath('image_urls', path_image, MapCompose(lambda i: 'http://www.sncf-connect.com' + i))

                ll=l.load_item()
                yield ll



