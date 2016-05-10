# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings

from Logger import *
logger = setupLogging(__name__)
logger.setLevel(INFO)


class BookmarksPipeline(object):

    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self):
        client = MongoClient(u'localhost', 27017)
        db = client[settings[u'MONGODB_DB']]
        self.collection = db[settings[u'MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        try:
            logger.debug(u"%s[%s]" % (item, type(item)))
            self.collection.insert(dict(item))

        except Exception, msg:
            logger.error(u"%s" % msg)

        return item
