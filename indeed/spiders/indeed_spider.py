from scrapy import Spider, Request
from indeed.items import indeedItem
import re


class indeedSpider(Spider):
	name = 'indeed_spider'
	allowed_urls = ['https://www.indeed.com/']
	companies=['Facebook','Amazon.com','Google','Netflix','Apple']
	start_urls=['https://www.indeed.com/companies']
	#start_urls=['https://www.indeed.com/cmp/' + company + '/reviews' for company in companies]
	
	print(start_urls)

	def parse(self, response):
		companies=['Facebook','Amazon.com','Google','Netflix','Apple']
		c_urls=['https://www.indeed.com/cmp/' + company + '/reviews' for company in companies]
		print('='*50)
		print('c_urls')
		print(c_urls)
		print('='*50)
		for url in c_urls:
			yield Request(url=url, callback=self.parse_page)

	def parse_page(self, response):

		num_rev = response.xpath('//div[@class="cmp-review-search-summary"]/span/b/text()').extract_first()
		num_rev=int(num_rev.replace(',',''))
		print('='*50)
		print('numRev')
		print(num_rev)
		print('='*50)
		page = (num_rev-1)//20 + 1
		print(page)

		
		url = [response.request.url +'?start='+str(i*20) for i in range(int(page))]
		print('='*50)
		print(url)
		print('='*50)


		#for url in self.start_urls:
		#	url_list = [url +'?start='+str(i) for i in range(0,int(num_rev),20)]
		#print(url_list)
		for u in url:
			print(u)
			yield Request(url=u, callback=self.parse_result_page)


	def parse_result_page(self, response):
		review_id=response.xpath('//div[@class="cmp-review-container"]')
		for review in review_id:

			title=review.xpath('.//div[@class="cmp-review-title"]/span/text()').extract()
			
			location=review.xpath('.//div[@class="cmp-review-subtitle"]/span[2]/text()').extract()
			
			date=review.xpath('.//div[@class="cmp-review-subtitle"]/span[3]/text()').extract()
			
			jobtitle=review.xpath('.//div[@class="cmp-review-subtitle"]/span/span/text()').extract()
			
			
			allreviews= review.xpath('.//div[@class="cmp-Rating cmp-Rating--normal cmp-Rating--middle"]').extract()

		
			company =response.xpath('.//div[@class="cmp-company-name"]/text()').extract_first()
			review_content = review.xpath('.//div[@class="cmp-review-description"]/span/text()').extract()
			
			print('='*50)
			print(review_content)
			print('='*50)
			
			all_reviews_num=[]

			for i in range(len(allreviews)):
				all_reviews_num.append(int(re.findall("\d+",allreviews[i])[0]))
				every_six_rev=[all_reviews_num[x:x+6] for x in range(0,len(all_reviews_num),6)]
			for individual_review in every_six_rev :
				tot_review=individual_review[0]
				Work_Life_review=individual_review[1]
				Comp_Benef_review=individual_review[2]
				Job_Security_Adv=individual_review[3]
				Management_review=individual_review[4]
				Job_Culture_review=individual_review[5]




			item = indeedItem()
			item['title'] = title
			item['location'] = location
			item['date'] = date
			item['jobtitle'] = jobtitle
			item['tot_review'] = tot_review
			item['Work_Life_review'] = Work_Life_review
			item['Comp_Benef_review'] = Comp_Benef_review
			item['Job_Security_Adv'] = Job_Security_Adv
			item['Management_review'] = Management_review
			item['Job_Culture_review'] = Job_Culture_review
			item['company'] = company
			item['review_content'] = review_content



			yield item


			
	

		
		
		

