# -*- coding: utf-8 -*-
import scrapy


class PnpspiderSpider(scrapy.Spider):
    name = 'pnpSpider'
    allowed_domains = ['api.ontario.ca']
    start_urls = ['http://api.ontario.ca/']

    def parse(self, response):
        pass
