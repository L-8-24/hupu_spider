#! /usr/bin/env python
# -*- coding:utf-8 -*-

from URLManager import URLManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from OutputData import OutputData

class HupuSpider(object):
	def __init__(self):
		self.manager = URLManager()

		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = OutputData()

	def crawl(self,root_url):
		self.manager.add_url(root_url)
		while(self.manager.has_newurls()):
			url = self.manager.get_new_url()
			html_cont = self.downloader.download(url)
			next_page = self.parser.get_nextpage(url,html_cont)
			print next_page
			self.manager.add_url(next_page)
			news_urls = self.parser.get_news_list(url,html_cont)
			for news_url in news_urls:
				news_cont = self.downloader.download(news_url)
				news = self.parser.get_news_content(news_url,news_cont)
				self.output.store_data(news)

if __name__ == '__main__':
	spider = HupuSpider()
	spider.crawl('https://voice.hupu.com/nba/1')