# -*- coding: utf-8 -*-
import os
from datetime import datetime
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from ..items import BookmarksItem

from ..Logger import *
logger = setupLogging(__name__)
logger.setLevel(INFO)

u"""
Note: Scrapy also adds the ::attr(attribute_name)
functional pseudo-element to extract attribute value (that's also not possible
with standard CSS selectors.

Example
site = ''.join(hxs.select("//h1[@class='state']/text()").extract()).strip()
"""


class LinksSpider(Spider):
    name = u"links"
    n = 0

    def __init__(self, *args, **kwargs):
        super(LinksSpider, self).__init__(*args, **kwargs)
        self.start_urls = loadList(u"bookmarks.pl")

        if False:
            for x in self.start_urls:
                logger.info(u"%s::%s" % (x, __name__))

    def parse(self, response):
        logger.debug(u"%s" % response)
        n = 0
        for sel in response.xpath(u"/html/body"):
            item = BookmarksItem()
            item[u'description'] = sel.xpath(u'//p/text()').extract()
            item[u"anchors"] = sel.xpath(u'//a/@href').extract()
            item[u"description"] = sel.xpath(u'//h1/text()').re(u'-\s[^\n]*\\r')
            item[u"last_updated"] = str(datetime.now())

            logger.debug(u"%s%d.parse.item : %20s" % (os.linesep, n, item[u'description']))
            n += 1
            yield item

    def __parse(self, response):
        self.n += 1
        logger.info(u"%d%s%s%s" % (self.n, os.linesep, __name__, os.linesep))

        item = BookmarksItem()

        if True:
            sel = Selector(response)
            item[u"description"] = sel.xpath(u"/html/body/text()").extract().strip()
            item[u'name'] = u"James"
        else:
            sel = response.xpath(u"/html/body/")
            item[u'name'] = sel.xpath(u'a/text()').extract()
            item[u'url'] = sel.xpath(u'a/@href').extract()
            item[u'description'] = sel.xpath(u'text()').re(u'-\s[^\n]*\\r')
            item[u"datetime"] = datetime.datetime()

        return item

    def _parse(self, response):
        l = ItemLoader(item=BookmarksItem(), response=response)
        l.add_xpath(u"name", u"/html/head/title")
        l.add_xpath(u"anchors", u"//a/@href'")
        l.add_xpath(u"description", u"/html/body/text()")
        l.add_value(u"last_updated", datetime.datetime)  # you can also use literal values
        return l.load_item()

