# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BaidunewPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="localhost", user="root", passwd="root", db="bdnew")
        for i in range(0,len(item["keyword"])):
            keyword = item["keyword"][i]
            title = item["title"][i]
            url = item["url"][i]
            sql = "insert into new(keyword,title,url) values" \
                  " ('" + keyword + "','" + title + "','"  + url + "')"
            try:
                conn.query(sql)
            except Exception as err:
                print(err)
        conn.close
        return item

