#!/usr/bin/python
# -*- encoding:utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
import requests
from lxml import html
import lxml.html
import json
from items import AnuncioItem

class AnuncioLister(CrawlSpider):
    name = 'app'
    item_count = 0
    main_url = 'https://lista.mercadolivre.com.br'

    print 'entre o termo para buscar: '
    product = str(raw_input())
    print 'entre o numero de itens para buscar: '
    m = int(raw_input())

    if product:
    	start_urls = ['%s/%s#D[A:%s]' % (main_url, product, product)]
    else:
    	start_urls = ['https://lista.mercadolivre.com.br/cookbook#D[A:cookbook]']

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="pagination_next"]/a'))),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[contains(@class, "item__title")]/a')),
            callback = 'parse_item', follow=False)
    }

    def parse_item(self, response):
        print 'Salvando de um anuncio'
        
        ml_anuncio = AnuncioItem()
        ml_anuncio['name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        ml_anuncio['link'] = response.url
        ml_anuncio['price'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
        #ml_anuncio['price_d'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
        ml_anuncio['store'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
        ml_anuncio['state'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()

        self.item_count += 1
        if self.m: 
            if self.item_count > self.m:
                raise CloseSpider('fim')
        else:
            if self.item_count > 10:
                raise CloseSpider('Fim')
        yield ml_anuncio

