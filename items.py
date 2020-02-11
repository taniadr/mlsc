#!/usr/bin/python
# -*- encoding:utf-8 -*-
import scrapy

class AnuncioItem(scrapy.Item):
#Definition of item to store the data from each aid
    name = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    store = scrapy.Field()
    state = scrapy.Field()