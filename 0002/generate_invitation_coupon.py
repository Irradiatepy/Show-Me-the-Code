# -*- coding:utf-8 -*-
import MySQLdb
import random
import string


def generate_invitation_coupon():
	coupons = []
	for num in range(200):
		str_num = "0" * (8 - len(str(num))) + str(num)
		coupon = ""
		for i in range(8):
			coupon += str_num[i] + random.choice(string.lowercase + string.uppercase + "~!@#$%^&*()_+-=")
		coupons.append((num, coupon))
	return coupons


def save_to_mysql(coupons):
	conn = MySQLdb.connect(host='localhost', user='root', passwd='js8023jj', port=3306, db='test')
	cur = conn.cursor()
	cur.execute("create table coupons(id int primary key, value varchar(32))")
	cur.executemany("insert into coupons values(%s, %s)", coupons)
	
	conn.commit()

	cur.close()
	conn.close()


if __name__ == '__main__':
	save_to_mysql(generate_invitation_coupon())
	















