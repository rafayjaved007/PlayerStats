# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerstatisticsItem(scrapy.Item):

    full_name = scrapy.Field()
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    team_name = scrapy.Field()
    apps = scrapy.Field()
    age = scrapy.Field()
    played_positions = scrapy.Field()
    rating = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    position = scrapy.Field()
    ranking = scrapy.Field()
    team_region_name = scrapy.Field()
