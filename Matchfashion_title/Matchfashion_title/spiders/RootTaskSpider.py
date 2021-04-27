import scrapy
import datetime
import uuid
import re
import random
import json
from Matchfashion_title.items import CategoryTree, ProductInfo
from Matchfashion_title.itemloader import CategoryTreeItemLoader, ProductInfoItemLoader
from scrapy.http.headers import Headers
from Matchfashion_title.settings import BOT_NAME


# class RoottaskspiderSpider(scrapy.Spider):
class RoottaskspiderSpider(scrapy.Spider):
    name = 'RootTaskSpider'
    allowed_domains = ['www.matchesfashion.com']
    start_urls = ['https://www.matchesfashion.com/fr/api/designers/mens/az']
    main_url = 'https://www.matchesfashion.com'

    def __init__(self, *args, **kwargs):
        # 修改这里的类名为当前类名
        super(RoottaskspiderSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        try:
            return self.getCategory(response=response)
        except Exception as err:
            print(err)

    # 获取目录
    def getCategory(self, response):
        success = response.status == 200
        if success:
            cate_list_1 = json.loads(response.text)  # 一级目录元素列表
            #data = response.body
            #data = data.decode(' GBK ',  'ignore')
            #with open("cate.html", "w") as out_file:
            print(cate_list_1[0])

            #    out_file.write(cate_list_1)
            for ele in cate_list_1:

                cate_1 = ele.get('letter')  # 一级目录  # 一级目录商品url
                a = ele.get('designers')
                for b in a:
                    cate_2 = b.get('name')
                    url = b.get('url')
                    item = self.getCategoryItem(
                        cate_1,
                        cate_2,
                        None,
                        url,
                        None
                    )
                    yield item



    def getCategoryItem(self, cate_1, cate_2, cate_3, url, c_rootId=''):
        category_tree = CategoryTree()
        category_itemloader = CategoryTreeItemLoader(item=category_tree)
        category_itemloader.add_value('Id', str(uuid.uuid4()))

        category_itemloader.add_value('ProjectName', BOT_NAME)
        category_itemloader.add_value('Level_Url', url)
        category_itemloader.add_value('CategoryLevel1', cate_1)
        category_itemloader.add_value('CategoryLevel2', cate_2)
        category_itemloader.add_value('CategoryLevel3', cate_3)

        # time = datetime.datetime.now().isoformat()
        # category_itemloader.add_value('CreateDateTime', time)
        # category_itemloader.add_value('UpdateDateTime', time)

        category_itemloader.add_value('RootId', c_rootId)

        # category_itemloader.add_value('ManufacturerId', 12)
        # category_itemloader.add_value('CategoryId', 20)

        item_load = category_itemloader.load_item()

        return item_load

    headers_list = [
        # Chrome
        {
            'authority': 'www.marionnaud.fr',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
            'sec-ch-ua-mobile': '?0',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en,fr;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        },
        # IE
        {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.7,en;q=0.5,zh-Hans-CN;q=0.3,zh-Hans;q=0.2",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19041",
        },
        # Firefox
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers',
        }
    ]



