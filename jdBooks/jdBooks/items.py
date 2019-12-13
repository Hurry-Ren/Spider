# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()    #栏目下的分类
    name = scrapy.Field()   #每类的名称
    book_name = scrapy.Field()  #每类下的书籍名
    book_price = scrapy.Field() #每类下的书籍价格
    book_author = scrapy.Field()#每类下的书籍作者
    book_store = scrapy.Field() #每类下的书籍商店
    book_comment = scrapy.Field() #每类下的书籍评论数
