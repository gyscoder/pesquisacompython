# -*- coding: UTF-8 -*-
__title__ = 'potato'
__version__ = '1.0.0'
__author__ = '@geysom'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 by Me'

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
	def __init__(self, texto):
		self.texto = texto
		print(texto)

	def inicio(self):
		self.googlesearch.get_random_user_agent()
		return