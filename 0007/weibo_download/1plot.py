# -*- coding:utf-8 -*-
#将education表中教育信息为大连理工大学的转移到dlut表中
import sys
import requests
import threading
import ConfigParser
from bs4 import BeautifulSoup
import time
import re
import MySQLdb
import random
from getconnect import GetConnect
from dlut import Dlut
from dlut_db import Dlut_Db

from pylab import *

##################################################################################################
def conveyToSchoolTable(schoolname):
	'将education表中所有大连理工大学的微博用户添加到dlut表中'
	global GetConnect
	sql = "select * from education where school = '%s'" % schoolname
	myconnect = GetConnect()
	results = myconnect.getData(sql)
	dlut_d = Dlut_Db()
	if results:
		for r in results:
			dluters = Dlut(r[1])
			dlut_d.insertIntoDB(dluters)
			#print r[1]
		countsql = "select * from dlut"
		count = myconnect.getCount(countsql)
		return count

def plotSexRatio():
	
##################################################################################################
def main():
	schoolname = u'大连理工大学'
	schoolIdCount = conveyToSchoolTable(schoolname)
	print 'There are %s number of dlut students now' % schoolIdCount

if __name__ == '__main__':
	main()
