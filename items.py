import scrapy

class AnuncioItem(scrapy.Item):
#Definition of item to store the data from each aid
    name = scrapy.Field()
    link = scrapy.Field()
    price_f = scrapy.Field()
    price_d = scrapy.Field()
    store = scrapy.Field()
    state = scrapy.Field()
