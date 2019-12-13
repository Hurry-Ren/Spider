# -*- coding: utf-8 -*-
import scrapy
import re
from jdBooks.items import JdbooksItem

from jdBooks.spiders.culumn import column

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://channel.jd.com/p_wenxuezongheguan.html']

    # 找价格，书名，评论等
    def parse(self, response):
        items = JdbooksItem()
        url = response.xpath('//div[@class="ext"]/p/a/@href').extract()  # 栏目下的分类链接
        name = response.xpath('//div[@class="ext"]/p/a/@title').extract()  # 每类的名称
        # 查询每个分类
        for i in range(0, len(url)):
            # scrapy.Request发请求时，必须要完整的URL信息,所以要加https://
            targetUrl = 'https:'+url[i]
            items['book_name'],items['book_price'],items['book_author'],\
            items['book_store'],items['book_comment']= column(targetUrl)
            for j in range(0,len(items['book_name'])):
                items['book_name'][j] = re.sub(r'\s+', '', items['book_name'][j])
            yield items









