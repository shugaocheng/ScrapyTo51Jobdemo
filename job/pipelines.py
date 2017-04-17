# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymysql.cursors
from job import settings

class JobPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = "insert into bookmarks.job(jingyan,xinzi,gzdd,fbrq,gsname,gwname,renshu,sbdz,xueli) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        try:
            self.cursor.execute(sql,(item['jingyan'],item['xinzi'],item['gzdd'],item['fbrq'],
                                     item['gsname'],item['gwname'],item['renshu'],item['sbdz'],item['xueli']))
            self.connect.commit()
        except Exception as error:
            print(error)
            self.connect.rollback()
        return item