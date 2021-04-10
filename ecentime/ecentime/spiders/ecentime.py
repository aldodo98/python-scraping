import scrapy
from ecentime.items import EcentimeItem
from lxml import html
import re

class Opp2Spider(scrapy.Spider):

    name = 'Ecentime'
    allowed_domains = ['ecentime.com']
    offset = 1
    start_urls = ("https://www.ecentime.com/mall",)

    def parse(self, response):

        items = []

        data = response.body.decode()
        position_pat =re.compile('<div class="mall-list-name" data-v-088d4c67>.*?</div></a><div class="mall-link"')
        list = position_pat.finditer(data)
        for i in list:
            #m = re.search('(?<=.html">)', i)
            m = i.group()
            m = m.split(">")
            M = m[1]
            M = M[:-5]
            item = EcentimeItem()
            item['name'] = M
            #items.append(item)
            yield item

        print("第{0}页爬取完成".format(self.offset))
        if self.offset < 13: #爬前几页
            self.offset += 1
        url2 = ("https://www.ecentime.com/mall?page="+str(self.offset))
        yield scrapy.Request(url=url2, callback=self.parse)

        #List = re.split('\W+', list)

        #with open(filename, 'w', encoding='utf-8') as f:
        #    f.write(response.body.decode())

