# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib2


# 找出一个网页的所有的正文
def find_texts(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}  
	req = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html).body
	for line in soup.text.encode('utf-8').split('\n'):
		if line != '' and repr(line.strip(' \r')) != "''":
			print (line.strip(' \r'))


def find_texts_2(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.text).body
	for line in soup.text.encode('utf-8').split('\n'):
		if line != '' and repr(line.strip(' ')) != "''":
			print line.strip(' ')



if __name__ == '__main__':
	urls = ['http://www.baidu.com', 'http://blog.csdn.net/whiterbear', 'https://github.com']
	find_texts(urls[1])
	# find_texts_2(urls[2])


