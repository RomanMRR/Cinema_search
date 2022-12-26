# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BestmoviesItem(scrapy.Item):
    rating = scrapy.Field()
    name_russian = scrapy.Field()
    name_english = scrapy.Field()
    year = scrapy.Field()
    kinopoisk_rating = scrapy.Field()
