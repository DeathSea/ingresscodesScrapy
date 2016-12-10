# -*- coding:utf-8 
import scrapy
class pageSpider(scrapy.Spider):
	name = "page"
	start_urls = ["https://ingress.codes"]

	def parse(self,response):
		#response.css("article")[0].css("a")[0].re("https://ingress.codes/\d{4}/\d{2}/\d{2}/[\w-]*/")
		for post in response.css("article"):
			yield scrapy.Request(post.css("a::attr(href)").extract_first(),callback = self.parse_post)
		next_page = response.css("nav.navigation div.nav-links a.next::attr(href)").extract_first()

		self.log("the next page:"+next_page)
		if next_page is not None:
			yield scrapy.Request(next_page, callback = self.parse)


	def parse_post(self,response):
		this_post_title = response.css("h1.entry-title::text").extract_first().replace("|","").replace("<","").replace(">","").replace("\\","").replace("/","").replace(":","").replace("?","").replace("*","").replace("\"","")
		this_post_content = response.css("div.entry-content").extract_first().encode("utf-8")
		tags = []
		for tag in response.css("span.cat-links a::text"):
			tags.append(tag.extract())
		self.log("this tags is:"+str(tags))
		# self.log(u"this content is:"+this_post_content)
		if u"Daily Codes" in tags:
			#invest ingress code
			code_collection = response.css("code::text").re("\[\w{1,2}\]\xa0([a-zA-Z0-9]*)")
			with open("code_post_map.txt","a") as f:
				for code in code_collection:
					print >> f,code,this_post_title.encode("utf-8")

			with open("code\\%s.html"%this_post_title,"w") as f:
				f.write(this_post_content)


		elif u"Ingress Report" in tags:
			#ingress report code
			with open("code_post_map.txt","a") as f:
				for code in code_collection:
					print >> f,code,this_post_title.encode("utf-8")

			with open("code\\%s.html"%this_post_title,"w") as f:
				f.write(this_post_content)


		elif u"Special Missions" in tags:
			with open("Special Missions\\%s.html"%this_post_title,"wb") as f:
				f.write(this_post_content)

		elif u"WOTD Puzzles" in tags:
			with open("WOTD Puzzles\\%s.html"%this_post_title,"wb") as f:
				f.write(this_post_content)


		elif u"Anomaly Codes" in tags:
			with open("Anomaly Codes\\%s.html"%this_post_title,"wb") as f:
				f.write(this_post_content)

		elif u"Tutorials" in tags:
			with open("Tutorials\\%s.html"%this_post_title,"wb") as f:
				f.write(this_post_content)

		else:
			with open("unkown\\%s.html"%this_post_title,"wb") as f:
				f.write(this_post_content)
