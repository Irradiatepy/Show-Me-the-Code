# -*- coding:utf-8 -*-
import random
import string


def generate_invitation_coupon():
	for num in range(200):
		str_num = "0" * (8 - len(str(num))) + str(num)
		coupon = ""
		for i in range(8):
			coupon += str_num[i] + random.choice(string.lowercase + string.uppercase + "~!@#$%^&*()_+-=")
		print coupon


if __name__ == '__main__':
	generate_invitation_coupon()