#!/usr/bin/env python
# -*- coding:utf-8 -*-
import web
urls = (
	'/hello','Index'
)
app = web.application(urls, globals())
render = web.template.render('/home/tuopan/PycharmProjects/git_tensorflow/tensorflow/LearningPythonHard/projects/gothonweb/templates')
class Index(object):
	def GET(self):
		#form = web.input(name = "Nobody",greet = None)
		#if form.greet:
		#	greeting = "%s,%s"% (form.greet, form.name)
		#	return render.index(greeting = greeting)
		#else:
		#	return "ERROR:greet is required."
		return render.hello_form()
	def POST(self):
		form = web.input(name = "Nobody", greet = "Hello")
		greeting = "%s, %s"%(form.greet, form.name)
		return render.index(greeting = greeting)
if __name__ == "__main__":
	app.run()
