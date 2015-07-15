# -*- coding:utf-8 -*-
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def count_code(dir_name):
	# code_file_ends = ['.py', '.c', '.cpp', '.java']
	code_counts = {'code':0, 'blank':0, 'annotation':0}
	if os.path.exists(dir_name):
		file_list = os.listdir(dir_name)
		code_file_list = [file_name for file_name in file_list if file_name[-3:] == '.py']
		# print code_file_list
		for code_file in code_file_list:
			print code_file
			# print '-'*100
			for line in open(os.path.join(dir_name, code_file)):
				# print (line),
				if re.match('#', line.strip()) is not None or re.match('\'', line.strip()) is not None or re.match("\"", line.strip()) is not None:
					# print 'annotation'
					code_counts['annotation'] = code_counts.get('annotation', 0) + 1
				elif re.search('[^\s]', line) is not None:
					# print 'code'
					code_counts['code'] = code_counts.get('code', 0) + 1
				else:
					# print 'blank'
					code_counts['blank'] = code_counts.get('blank', 0) + 1

		print "annotation is %s line, blank is %s line, code is %s line" % (code_counts['annotation'], code_counts['blank'], code_counts['code'])


	else:
		print "There is no file named:%s" % dir_name


if __name__ == '__main__':
	count_code('weibo_download')