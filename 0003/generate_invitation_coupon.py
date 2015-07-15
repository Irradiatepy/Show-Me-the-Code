# -*- coding:utf-8 -*-
import redis
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


def save_to_redis(coupons):
	r = redis.Redis(host='localhost', port=6379, db=0)
	for coupon in coupons:
		r.lpush('coupons', coupon)
	print r.lrange('coupons', start=0, end=10)


if __name__ == '__main__':
	save_to_redis(generate_invitation_coupon())
	















