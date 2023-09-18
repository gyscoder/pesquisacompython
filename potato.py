# -- coding: UTF-8 --
_title_ = 'potato'
_version_ = '1.0.0'
_author_ = '@geysom'
_license_ = 'MIT'
_copyright_ = 'Copyright 2020 by Me'

try:
	from googlesearch import search
except ImportError:
	print("dammmm..")

import googlesearch
import os
import sys
from pyfiglet import Figlet
from datetime import datetime

class batataAssada():
	def _init_(self):
		self.user_agent = googlesearch.get_random_user_agent()
		#self.config(query, tld, lang, num, stop, pause, user_agent)

	def config(self, query, tld, lang, num, stop, pause, user_agent):
		custom_fi = Figlet(font='epic')
		print(custom_fi.renderText('  potato  '))
		data = str(datetime.today())
		print('[+] Começando em {} [+]'.format(data[0:19]))
		print('[+] Usando o agente {} [+]\n'.format(user_agent))
		print('[+] Resultado: [+]\n')

		try:
			for j in search(query=query, tld=tld, lang=lang, num=int(num), stop=int(stop), pause=int(pause), user_agent=user_agent):
				print('[getting url] ' + j)
		except SyntaxError:
			print('try: '+ _file_ + ' search (query you want to use) com(top level domain) language(pt-br, en) num(number of urls, eg. 10)')
			print('example: '+ _file_ + ' noticias com pt-br 50')

try:
	batataAssada().config(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], 'user_agent')
	#batataAssada().config('teste', 'com', 'pt-br', 10, 10, 5, 'user_agent')
except IndexError:
	print('try: '+sys.argv[0]+ ' search (query you want to use) com(top level domain) language(pt-br, en) num(number of urls, eg. 10), stop(limit), pause(time)')
	print('example: '+sys.argv[0]+ ' noticias com pt-br 50 20 5')