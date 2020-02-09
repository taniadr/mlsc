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
    m = 15
    main_url = 'https://lista.mercadolivre.com.br'


    print 'entre o termo para buscar: ',
    product = raw_input()    	

    #print 'entre o numero de itens para buscar: ',
    #m = int(raw_input())

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
    
        #links_noticias = response.xpath('//h2[re:test(@class, "item__title list-view-item-title")]/a[re:test(@href,"")]/@href').extract()

        #colocar uma condição para paginação e um segundo call back por causa do time pra carregar a pagina
        #https://scrapy.readthedocs.io/en/latest/topics/request-response.html#topics-request-response-ref-request-callback-arguments
        print 'Salvando de um anuncio'
    		
    	ml_anuncio = AnuncioItem()
    	ml_anuncio['name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
    	ml_anuncio['link'] = response.url
    	ml_anuncio['price_f'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
    	ml_anuncio['price_d'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
    	ml_anuncio['store'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
    	ml_anuncio['state'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()

        self.item_count += 1

        if self.item_count > 20:
            raise CloseSpider('item_exceeded')
        yield ml_anuncio

class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self, data):
        sys.stdout.write("\r"+data.__str__())
        sys.stdout.flush()
