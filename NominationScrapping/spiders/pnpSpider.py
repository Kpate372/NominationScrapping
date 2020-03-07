# -*- coding: utf-8 -*-
import scrapy
import datetime
from NominationScrapping.spiders import emailLogic as el
from NominationScrapping.spiders import dbConnector as dc

class PnpspiderSpider(scrapy.Spider):
    name = 'pnpSpider'
    allowed_domains = ['api.ontario.ca']
    start_urls = ['https://api.ontario.ca/api/drupal/page%2F2020-ontario-immigrant-nominee-program-updates?fields=nid,field_body_beta,body']

    def parse(self, response):
        todayDate = datetime.datetime.now()
        dateString = todayDate.strftime("%B %-d, %Y")
        #dateString = "March 6, 2020"
        data = response.text
        match = data.find(dateString)
        if match > -1:
            noOfTimes = data.count(dateString)/2
            if dc.checkForEmail(dateString, noOfTimes):
                print(str(todayDate)+"-----Update is there and email already sent")
            else:
                el.sendEmail()
                print(str(todayDate)+"*****Update is there and email just sent*****")
        else:
            print(str(todayDate)+"-----No Update Found-----")

