# -*- coding:utf-8
import web,os
        
urls = (
    '/', 'index',
    '/code/(.*?).html','html',
)
app = web.application(urls, globals())
render = web.template.render('templates/')
db = web.database(dbn='sqlite',db='test.db')
sep = os.sep
# for x in db.select('passcode'):
# 	print x
class index:
    def GET(self):
    	c = db.select('passcode')
        return render.test(content=c)

class html:
	def GET(self,html_name):
		content = '404 not found'
		# print html_name
		try:
			f = open('..'+sep+'code'+sep+'%s.html'%html_name,"r")
			content = f.read()
			f.close()
		except Exception,p:
			print p
		return render.pagemodel(title=html_name,content=content)

if __name__ == "__main__":
    app.run()
