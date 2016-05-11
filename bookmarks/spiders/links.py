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
        logger.debug(u"%s\%s" % (__name__, response))
        n = 0

        for sel in response.xpath(u"/html"):
            item = BookmarksItem()
            item[u"title"] = sel.xpath(u"//title/text()").extract()
            item[u'keywords'] = sel.xpath(u"//meta[@name='keywords']/text()").extract()
            item[u"description"] = sel.xpath(u"//meta[@name='description']/text()").extract()
            # item[u"anchorss"] = sel.xpath(u'//a/@href').extract()
            item[u"anchors"] = sel.xpath(u"//a[contains(@href, 'http')]/@href").extract()
            item[u"last_updated"] = str(datetime.now())

            n += 1
            yield item

    def _parse(self, response):
        l = ItemLoader(item=BookmarksItem(), response=response)
        l.add_xpath(u"name", u"/html/head/title")
        l.add_xpath(u"anchors", u"//a/@href'")
        l.add_xpath(u"description", u"/html/body/text()")
        l.add_value(u"last_updated", datetime.datetime)  # you can also use literal values
        return l.load_item()
