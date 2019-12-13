# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class PigPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="localhost", user="root", passwd="root", db="dangdang")
        for i in range(len(item["title"])):
            title = item["title"][i]
            price = item["price"][i]
            review = item["review"][i]
            url = item["url"][i]
            sql = "insert into goods(title,price,review,url) values" \
                  " ('" + title + "','" + price + "','" + review + "','" + url + "')"
            try:
                conn.query(sql)
            except Exception as err:
                print(err)
        conn.close
        return item
