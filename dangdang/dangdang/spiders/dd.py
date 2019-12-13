# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cid4001075.html']

    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@name='itemlist-title']/text()").extract()
        item["url"] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["review"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        print(item["price"])
        yield item      #将数据提交到pipelines
        for i in range(2,21):
            url = 'http://category.dangdang.com/pg'+str(i)+'-cid4001075.html'
            #print(url)
            yield Request(url,callback = self.parse)