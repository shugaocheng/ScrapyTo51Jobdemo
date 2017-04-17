# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    gsname = scrapy.Field() # 公司名
    gsrs = scrapy.Field() # 公司人数
    xueli = scrapy.Field() # 学历
    renshu = scrapy.Field() # 招聘人数
    jingyan = scrapy.Field() # 经验
    gwname = scrapy.Field()  # 职位名
    gzdd = scrapy.Field() # 工作地点
    xinzi = scrapy.Field() # 薪水
    fbrq = scrapy.Field() # 发布日期
    gwzz = scrapy.Field() # 岗位职责
    rzyq = scrapy.Field() # 任职要求
    sbdz = scrapy.Field() # 上班地址
    url = scrapy.Field() # 链接
