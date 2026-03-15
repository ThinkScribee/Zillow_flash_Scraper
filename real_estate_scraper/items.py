# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealEstateScraperItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    address = scrapy.Field()
    time_on_market = scrapy.Field()
    price = scrapy.Field()