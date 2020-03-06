# -*- coding: utf-8 -*-
import scrapy
import datetime
import spiders.emailLogic as el
import spiders.dbConnector as dc

class PnpspiderSpider(scrapy.Spider):
    name = 'pnpSpider'
    allowed_domains = ['api.ontario.ca']
    start_urls = ['https://api.ontario.ca/api/drupal/page%2F2020-ontario-immigrant-nominee-program-updates?fields=nid,field_body_beta,body']

    def parse(self, response):
        #todayDate = datetime.datetime.now()
        #dateString = todayDate.strftime("%B %-d, %Y")
        dateString = "March 4, 2020"
        data = response.text
        match = data.find(dateString)
        if match > -1:
            if dc.checkForEmail(dateString):
                print("\n\n\n\nUpdate is there and email already sent\n\n\n\n")
            else:
                el.sendEmail()
                print("\n\n\n\nUpdate is there and email just sent\n\n\n\n")
        else:
            print("No Update Found")

