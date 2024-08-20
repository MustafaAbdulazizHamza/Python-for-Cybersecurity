# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyfwdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    Price_exc_tax = scrapy.Field()
    price_inc_tax = scrapy.Field() 
    tax = scrapy.Field()
    availability = scrapy.Field()
    number_of_reviews = scrapy.Field()
    number_of_stars = scrapy.Field()
    description = scrapy.Field()
    genre  = scrapy.Field()