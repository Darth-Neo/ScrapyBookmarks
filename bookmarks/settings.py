# -*- coding: utf-8 -*-

# Scrapy settings for bookmarks project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

#
#  Scrapy settings for news project
#
SPIDER_MODULES = [u'bookmarks.spiders']
NEWSPIDER_MODULE = u'bookmarks.spiders'
DEFAULT_ITEM_CLASS = u'bookmarks.items.BookmarksItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = u"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"

# ITEM_PIPELINES = {'bookmarks.pipelines.BookmarksPipeline': 1}
ITEM_PIPELINES = {u'bookmarks.pipelines.MongoDBPipeline': 1}

MONGODB_SERVER = u"localhost"
MONGODB_PORT = 27017
MONGODB_DB = u"Bookmarks"
MONGODB_COLLECTION = u"Links"
