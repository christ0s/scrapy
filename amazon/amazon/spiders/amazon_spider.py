# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    #allowed_domains = ['amazon.com']
    start_urls = [
    'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1573242332&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        # product_names = response.css('.a-color-base.a-text-normal::text').extract()
        # print('skata' * 30)
        # print(product_names)
        # product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        # product_price = response.css('.a-spacing-top-small .a-price span').css('::text').extract()
        # product_rating = response.css('.a-size-small .a-link-normal .a-size-base').css('::text').extract()
        item = AmazonItem()
        page = response.css('.s-include-content-margin')
        for book in page:
        	# print(book.get())
        	# print(book.css('.a-color-base.a-text-normal::text').get())
        	product_name = book.css('.a-color-base.a-text-normal::text').get()
        	try:
        		product_author = book.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').get().strip()
        	except:
        		product_author = "Unkown"
        	product_price = book.css('.a-spacing-top-small .a-price span').css('::text').get()
        	product_rating = book.css('.a-size-small .a-link-normal .a-size-base').css('::text').get()
        	item['product_name'] = product_name
        	item['product_author'] = product_author
        	item['product_price'] = product_price
        	item['product_rating'] = product_rating

        	yield item
          			

            #    'title': book.css('.a-color-base.a-text-normal::text').get(),
                # 'author': quote.xpath('span/small/text()').get(),
            

        # page = AmazonPage()

        # page['product_name'] = product_name
        # items['product_author'] = product_author
        # items['product_price'] = product_price
        # items ['product_rating'] = product_rating

       

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+ str(AmazonSpiderSpider.page_number) +'&fst=as%3Aoff&qid=1573243255&rnid=1250225011&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 3 :
        	AmazonSpiderSpider.page_number += 1
        	yield response.follow(next_page, callback = self.parse)        