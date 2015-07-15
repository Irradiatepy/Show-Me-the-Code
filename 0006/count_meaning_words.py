# -*- coding:utf-8 -*-
import os
from collections import Counter

def count_meaning_words(dir_name):
	stop_words = open('stop_words').readline().split(' ')
	if os.path.exists(dir_name):
		file_list = os.listdir(dir_name)[1:]
		for f in file_list:
			# print f
			word_count = {}
			for line in open(os.path.join(dir_name, f)):
				words = line.strip().split(' ')
				for word in words:
					# 过滤掉停止词
					if word.lower() not in stop_words:
						word_count[word] = word_count.get(word, 0) + 1
			# for word_c in word_count:
			# 	print word_c, word_count[word_c]
			word_cc = Counter(word_count)
			print word_cc.most_common(10)
			print '-' * 100
	else:
		print 'There is no file named: %s' % dir_name


if __name__ == '__main__':
	count_meaning_words('diary')