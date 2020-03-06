# -*- coding: utf-8 -*-
import scrapy
import datetime
import NominationScrapping.spiders.emailLogic as el


class PnpspiderSpider(scrapy.Spider):
    name = 'pnpSpider'
    allowed_domains = ['api.ontario.ca']
    start_urls = ['https://api.ontario.ca/api/drupal/page%2F2020-ontario-immigrant-nominee-program-updates?fields=nid,field_body_beta,body']
    date = ''
    flag = False

    def parse(self, response):
        todayDate = datetime.datetime.now()
        dateString = todayDate.strftime("%B %-d, %Y")
        data = response.text
        match = data.find(dateString)
        if match > -1:
            if self.date == dateString:
                if self.flag == False:
                    el.sendEmail()
            else:
                self.date = dateString
                self.flag = True
                el.sendEmail()

