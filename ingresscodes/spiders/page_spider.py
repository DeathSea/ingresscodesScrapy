# -*- coding:utf-8 
import scrapy
from post_spider import postSpider
class pageSpider(scrapy.Spider):
	name = "page"
	start_urls = ["https://ingress.codes"]

	def parse(self,response):
		#response.css("article")[0].css("a")[0].re("https://ingress.codes/\d{4}/\d{2}/\d{2}/[\w-]*/")
		s = postSpider()
		for post in response.css("article"):
			yield scrapy.Request(post.css("a::attr(href)").extract_first(),callback = s.parse)
		next_page = response.css("nav.navigation div.nav-links a.next::attr(href)").extract_first()

		# self.log("the next page:"+next_page)
		if next_page is not None:
			yield scrapy.Request(next_page, callback = self.parse)