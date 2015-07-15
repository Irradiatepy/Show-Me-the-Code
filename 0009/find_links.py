# -*- coding:utf-8 -*-
import requests
import urllib2
import re


# 找出一个网页的所有的链接
def find_urls(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}  
	req = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(req)
	link_regex = r"('|\")(https?://[^\s]+)('|\")"
	html = response.read()
	urls = re.findall(link_regex, html)
	for url in urls:
		print url[1]


def find_urls_2(url):
	req = requests.get(url)
	link_regex = r"('|\")(https?://[^\s]+)('|\")"
	urls = re.findall(link_regex, req.text)
	for url in urls:
		print url[1]
	# print '', req.text.encode('utf-8')


if __name__ == '__main__':
	urls = ['http://www.baidu.com', 'http://blog.csdn.net/whiterbear', 'https://github.com']
	# find_urls(urls[1])
	find_urls_2(urls[2])