import scrapy
from mySpider.items import ItcastItem
from lxml import html
import re
class Opp2Spider(scrapy.Spider):

    name = 'itcast'
    allowed_domains = ['55haitao.com']
    offset = 1
    start_urls = ("https://www.55haitao.com/store/list/0-23-0-0-all-"+str(offset)+".html",)


    def parse(self, response):
        #open("teacher.html","wb").write(response.body).close()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        items = []
        filename = "55.html"
        data = response.body.decode()
        position_pat =re.compile('html">.*?</a>.*\n.*')
        list = position_pat.finditer(data)

        for i in list:
            #m = re.search('(?<=.html">)', i)
            m = i.group()
            m = m.split(">")
            M = m[1]
            M = M[:-3]
            n = m[-1]
            n = n[15:]
            item = ItcastItem()
            item['name'] = M
            item['remise'] = n
            items.append(item)
            yield item

        print("第{0}页爬取完成".format(self.offset))
        if self.offset < 1: #爬前几页
            self.offset += 1
            url2 = ("https://www.55haitao.com/store/list/0-8-0-0-all-"+str(self.offset)+".html")
            yield scrapy.Request(url=url2, callback=self.parse)

        #List = re.split('\W+', list)

        #with open(filename, 'w', encoding='utf-8') as f:
        #    f.write(response.body.decode())

