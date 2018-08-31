# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    #省份
    province = scrapy.Field()
    #城市
    city = scrapy.Field()
    #楼盘名称
    name = scrapy.Field()
    #价格
    price = scrapy.Field()
    #几居室
    rooms = scrapy.Field()
    #面积
    area = scrapy.Field()
    #地址
    address = scrapy.Field()
    #行政区
    district = scrapy.Field()
    #是否在售
    sale = scrapy.Field()
    #详情页面
    origin_url = scrapy.Field()

