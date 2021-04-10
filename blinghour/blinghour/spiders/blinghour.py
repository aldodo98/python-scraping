import scrapy
from blinghour.items import Blinghour
from lxml import html
import re

class Opp2Spider(scrapy.Spider):

    name = 'Blinghour'
    allowed_domains = ['blinghour.com']

    start_urls = ("https://www.blinghour.com/shops.html",)

    def parse(self, response):

        items = []

        data = response.body.decode()
        position_pat =re.compile('html">[\u4e00-\u9fa5].*?</a></li>')
        list = position_pat.finditer(data)

        n = 0
        for i in list:
            n += 1
            if n > 182:
                m = i.group()
                m = m.split(">")
                M = m[1]
                M = M[:-3]
                M = M.split(" ")
                item = Blinghour()
                item['name'] = M[1]
                item['pays'] = M[0]

                #print(item['pays'])
                #items.append(item)
                yield item

        #List = re.split('\W+', list)

        #with open(filename, 'w', encoding='utf-8') as f:
        #    f.write(response.body.decode())

