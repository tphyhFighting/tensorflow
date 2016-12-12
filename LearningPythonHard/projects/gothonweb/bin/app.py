#!/usr/bin/env python
# -*- coding:utf-8 -*-
import web
import sys
sys.path.append('..')
from gothonweb import map
web.config.debug = False
urls = (
	'/game','GameEngine',
	'/','Index'
)
app = web.application(urls, globals())
if web.config.get('_session') is None:
	store = web.session.DiskStore('session')
	session = web.session.Session(app,store,initializer = {'room':None})
	web.config._session = session
else:
	session = web.config._session
render = web.template.render('/home/tuopan/PycharmProjects/git_tensorflow/tensorflow/LearningPythonHard/projects/gothonweb/templates/',base = 'layout')
class Index(object):
	def GET(self):
		#this is used to 'setup' the session with starting values
		session.room = map.START
		web.seeother("/game")
class GameEngine(object):
	def GET(self):
		if session.room:
			return render.show_room(room = session.room)
		else:
			#why is there here? do you need it?
			return render.you_died()
	def POST(self):
		form = web.input(action = None)
		#there is a bug here,can you fix it ?
		if session.room and form.action:
			session.room = session.room.go(form.action)
		web.seeother("/game")
#class count:
#	def GET(self):
		#form = web.input(name = "Nobody",greet = None)
		#if form.greet:
		#	greeting = "%s,%s"% (form.greet, form.name)
		#	return render.index(greeting = greeting)
		#else:
		#	return "ERROR:greet is required."
		#return render.hello_form()
#		session.count += 1
#		return str(session.count)
	#def POST(self):
	#	form = web.input(name = "Nobody", greet = "Hello")
	#	greeting = "%s, %s"%(form.greet, form.name)
	#	return render.index(greeting = greeting)
#class reset:
#	def GET(self):
#		session.kill()
#		return ""
if __name__ == "__main__":
	app.run()
