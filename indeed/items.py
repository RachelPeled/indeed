# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class indeedItem(scrapy.Item):

	title = scrapy.Field()
	location = scrapy.Field()
	date = scrapy.Field()
	jobtitle = scrapy.Field()
	tot_review = scrapy.Field()
	Work_Life_review = scrapy.Field()
	Comp_Benef_review = scrapy.Field()
	Job_Security_Adv = scrapy.Field()
	Management_review = scrapy.Field()
	Job_Culture_review = scrapy.Field()
	company = scrapy.Field()
	review_content =  scrapy.Field()