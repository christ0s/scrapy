import scrapy 

# from ..items import AmazonItem
class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	page_number = 2
	start_urls = ['http://quotes.toscrape.com/page/1/']

	def parse (self, response):
		items = AmazonItem()
		all_div_quotes = response.css('div.quote')

		for quotes in all_div_quotes:

			title = quotes.css('span.text::text').extract()
			author = quotes.css('.author::text').extract()
			tag = quotes.css('.tag::text').extract()
			items['title'] = title
			items['author'] = author
			items['tag'] = tag
			yield  items
		next_page = 'http://quotes.toscrape.com/page/1/' + str(QuoteSpider.page_number) +'/'
		#next_page = response.css('li.next a::attr{href)').get()
		print(next_page)
		
		if  QuoteSpider.page_number <11:
			QuoteSpider.page_number += 1 
			yield response.follow(next_page, callback=self.parse)


