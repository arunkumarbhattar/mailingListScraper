# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join


class Email(scrapy.Item):
    emailId = scrapy.Field()

    replyto = scrapy.Field(output_processor=Join())
    senderName = scrapy.Field(output_processor=Join())
    senderEmail = scrapy.Field(output_processor=Join())
    timeSent = scrapy.Field(output_processor=Join())
    timestampSent = scrapy.Field()
    timeReceived = scrapy.Field(output_processor=Join())
    timestampReceived = scrapy.Field()
    subject = scrapy.Field(output_processor=Join())
    body = scrapy.Field(output_processor=Join())
    url = scrapy.Field(output_processor=Join())

    pass
