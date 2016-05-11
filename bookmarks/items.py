# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class BookmarksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    keywords = Field()
    anchors = Field()
    description = Field()
    last_updated = Field(serializer=str)
