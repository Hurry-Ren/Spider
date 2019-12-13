# -*- coding: utf-8 -*-
import scrapy
from pig.items import PigItem
import re

class PigdataSpider(scrapy.Spider):
    name = 'pigData'
    allowed_domains = ['zhujia.zhuwang.cc']
    start_urls = ['https://zhujia.zhuwang.cc/index/api/chartData?areaId=440000']

    def parse(self, response):
        item = PigItem()
        data = response.read().decode("utf-8", "ignore")
        province_target = '"pigprice":([\s\S]*?)]'
        data_province = re.compile(province_target).findall(data)
        print(data_province)
        print('110')

