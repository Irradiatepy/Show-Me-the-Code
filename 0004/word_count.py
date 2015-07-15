# -*- coding:utf-8 -*-

# 任一个英文的纯文本文件，统计其中的单词出现的个数。

word_count = {}
for line in open('test_file', 'r'):
	if line != '\n':
		words = line.strip().split(' ')

	for word in words:
		word_count[word] = word_count.get(word, 0) + 1
for word_c in word_count:
	if 10 > word_count[word_c] > 1:
		print word_c, word_count[word_c]
