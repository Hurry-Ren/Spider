# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PigItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()
    pig_out = scrapy.Field()
    pig_in = scrapy.Field()
    pig_local = scrapy.Field()
    maizeprice = scrapy.Field()
    bean = scrapy.Field()

