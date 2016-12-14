# -*- coding:utf-8 
import scrapy
class postSpider(scrapy.Spider):
	name = "post"
	start_urls = ['https://ingress.codes/2016/12/12/the-challenges-ahead/','https://ingress.codes/2016/12/13/the-finish-line/']

	def parse(self,response):
		#fuck window dir
		this_post_title = response.css("h1.entry-title::text").extract_first().replace("|","").replace("<","").replace(">","").replace("\\","").replace("/","").replace(":","").replace("?","").replace("*","").replace("\"","").replace(u"\u2019","'")
		this_post_content = response.css("div.entry-content").extract_first().encode("utf-8")
		this_post_tag = response.css("div.tagcloud").extract_first()
		tags = []
		for tag in response.css("span.cat-links a::text"):
			tags.append(tag.extract())
		self.log("this tags is:"+str(tags))


		if u"Special Missions" in tags:
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


		elif u"Daily Codes" in tags or u"Ingress Report" in tags or u"Codes" in tags:
			#add the tag into post content
			if this_post_tag!= None:
				this_post_content = this_post_content + this_post_tag.encode("u8")
			#decode method tag in this post
			decode_tag = []
			for i in response.css("div.tagcloud a::text"):
				decode_tag.append(i.extract())

			#find the encode passcode in this post
			code_collection = response.css("code::text").re("\[\w{1,2}\][\xa0 ](.*)")
			self.log("there is %d code in post %s"%(len(code_collection),response.url))
			#maybe can;t find any code in this method log it:
			if len(code_collection) == 0:
				with open("find_passcode_by_hand.log","a") as f:
					print >> f,"code\\%s.html"%this_post_title.encode("u8"),"\t",",".join(decode_tag)
			#write encode passcode to map file
			with open("code_post_map.txt","a") as f:
				for code in code_collection:
					try:
						print >> f,code.encode("u8"),"\t",\
						this_post_title.encode("utf-8"),"\t",\
						response.url,"\t",\
						"code\\%s.html"%this_post_title.encode("u8"),"\t",\
						",".join(decode_tag)
					except:
						self.log("error while write passcode "+code+" in post : "+response.url)
			#write post content to file
			with open("code\\%s.html"%this_post_title,"w") as f:
				f.write(this_post_content)


		else:
			with open("unkown\\%s.html"%this_post_title,"wb") as f:
				f.write(this_post_content)
