#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo
class OutputData(object):
	def __init__(self):
		self.client = pymongo.MongoClient('127.0.0.1:27017')
		self.db = self.client['hupu_news']

	def store_data(self,news):
		self.db.newsInfo.insert(news)