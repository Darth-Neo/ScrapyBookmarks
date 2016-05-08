# -*- coding: utf-8 -*-
from scrapy.spiders import Spider

from ..items import BookmarksItem

from ..Logger import *
logger = setupLogging(__name__)
logger.setLevel(INFO)


class LinksSpider(Spider):
    name = u"links"
    # allowed_domains = [u"foxnews.com"]
    # start_urls = (u'http://www.foxnews.com/',)

    def __init__(self):

        logger.info(u"cwd : %s" % os.getcwd())
        self.start_urls = loadList(u"bookmarks.pl")

    def parse(self, response):
        logger.debug(u"%s" % response)
        n = 0
        for sel in response.xpath(u'/html'):
            item = BookmarksItem()
            item[u'text'] = sel.xpath(u'//body').extract()
            logger.debug(u"%s%d.parse.item : %20s" % (os.linesep, n, item[u'text']))
            n += 1
            yield item
