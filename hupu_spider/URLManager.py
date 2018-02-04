#!/usr/bin/env python
# -*- coding:utf-8 -*-

class URLManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def has_newurls(self):
		'''
		判断是否还有未爬取的url
		'''
		return self.new_urls_size() != 0

	def get_new_url(self):
		'''
		获取一条新的url
		'''
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_url(self,url):
		'''
		增加单条url
		'''
		if url is None:
			return None
		if url not in self.new_urls and url not in self.old_urls: 
			self.new_urls.add(url)

	def add_urls(self,urls):
		'''
		增加多条url
		'''
		for url in urls:
			self.add_url(url)

	def new_urls_size(self):
		'''
		获取未爬取的url的大小
		'''
		return len(self.new_urls)

	def old_urls_size(self):
		'''
		获取已爬取的url的大小
		'''
		return len(self.old_urls)