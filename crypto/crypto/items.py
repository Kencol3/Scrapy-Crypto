# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CryptoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Symbol = scrapy.Field()
    MCap = scrapy.Field()
    Price = scrapy.Field()
    Vol = scrapy.Field()
    CSupply = scrapy.Field()
    DayChg = scrapy.Field()
   # MxSupply = scrapy.Field()
    #Symbol = scrapy.Field()
    #Source = scrapy.Field()
    #Pair = scrapy.Field()
 