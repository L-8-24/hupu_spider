#! /usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urlparse

class HtmlParser(object):

	def get_nextpage(self,now_url,html_cont):
		'''
		获得下一页的url即新的一个url
		'''
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		next_page = soup.find('a',class_='page-btn-prev',text='下一页')
		if next_page is not None:
			next_page = next_page.get('href')
			next_page = urlparse.urljoin(now_url,next_page)
			return next_page
		return None

	def get_news_list(self,now_url,html_cont):
		'''
		获取当前页面的所有新闻
		'''
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		news_lists = soup.find('div',class_='news-list').find_all('li')
		news_urls = set()
		for news_list in news_lists:
			news_url = news_list.find('div',class_='list-hd')
			if news_url is not None:
				news_url = news_url.find('a').get('href')
				news_urls.add(news_url)
		return news_urls

	def get_news_content(self,news_url,html_cont):
		'''
		获取某一条新闻的信息
		'''
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		news = {}
		title = soup.find('h1',class_='headline').get_text().strip()
		news['title'] = title
		news_source = soup.find('span',id='source_baidu').find('a').get_text()
		news['news_source'] = news_source
		news_source_url = soup.find('span',id='source_baidu').find('a').get('href')
		news['news_source_url'] = news_source_url
		news_time = soup.find('span',id='pubtime_baidu').get_text()
		news['news_time'] = news_time
		image_url = soup.find('div',class_='artical-importantPic').find('img').get('src')
		news['image_url'] = image_url
		news_content = soup.find('div',class_='artical-main-content').get_text()
		news['news_content'] = news_content
		news_editor = soup.find('span',id='editor_baidu').get_text()
		news['news_editor'] = news_editor
		print title
		return news
