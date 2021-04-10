import scrapy
from ecentime.items import EcentimeItem
from lxml import html #要用split来分隔字符
import re

class Opp2Spider(scrapy.Spider):

    name = 'Ecentime'
    allowed_domains = ['ecentime.com']
    offset = 1 #这个值用来控制翻页，在这一页完成之后，+1，然后知道循环结束
    start_urls = ("https://www.ecentime.com/mall",)  #起始网站

    def parse(self, response):  #解析函数，运行爬虫时就会调用

        items = []

        data = response.body.decode() #将网站的源代码decode成string格式
        position_pat =re.compile('<div class="mall-list-name" data-v-088d4c67>.*?</div></a><div class="mall-link"') #定义正则表达式，用来匹配
        list = position_pat.finditer(data) #findall是返回一个字符，finditer会以迭代的形式返回寻找到的值
        for i in list: #将每一个匹配找到的值
            #m = re.search('(?<=.html">)', i)
            m = i.group()
            m = m.split(">") #根据返回的结果进行分割
            M = m[1] #找到关键信息所在位置
            M = M[:-5] #将找到的string裁剪
            item = EcentimeItem()
            item['name'] = M #将值给到item
            #items.append(item)
            yield item #将item的值yield，可以看作不中断函数的return，而且更高效

        print("第{0}页爬取完成".format(self.offset)) #显示爬取进度
        if self.offset < 13: #爬前几页，爬13页就写13
            self.offset += 1
        url2 = ("https://www.ecentime.com/mall?page="+str(self.offset)) #下一页的url
        yield scrapy.Request(url=url2, callback=self.parse) #用新网站再一次调用parse函数

        #List = re.split('\W+', list)

        #with open(filename, 'w', encoding='utf-8') as f:
        #    f.write(response.body.decode())

