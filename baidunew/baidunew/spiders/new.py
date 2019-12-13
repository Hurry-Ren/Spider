# -*- coding: utf-8 -*-

#要求：抓取整个页面全部新闻（标题，链接）
#难点：ajax数据的更新，数据的提取
#结果：成功啦啦啦
import scrapy
from baidunew.baidunew.items import BaidunewItem
from baidunew.baidunew.spiders.first import first
from baidunew.baidunew.spiders.second import second


class NewSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):
        item = BaidunewItem()

        #处理首页数据
        item['keyword'],item['url'],item['title'] = first(response)
        #print(item['title'][0])
        yield item

        #处理ajax（只处理了一部分适配数据，其他的同理）
        item['keyword'], item['url'],item['title'] = second()
        #print(item['title'][0])
        yield item                  #需要两次yield数据，不然之前的数据会被覆盖

        #json数据类没去处理，原则上和second一样。
