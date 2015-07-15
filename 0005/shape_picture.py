# -*- coding:utf-8 -*-
from PIL import Image


def shape_pic_size(image_name, normal_size):
	im = Image.open(r'./%s' % image_name)
	old_x, old_y = im.size

	cmp_x = old_x*1.0 / normal_size[0]
	cmp_y = old_y*1.0 / normal_size[1]

	cmp_n = cmp_x if cmp_x > cmp_y else cmp_y

	if cmp_n > 1.0:
		new_x = old_x / cmp_n
		new_y = old_y / cmp_n
		im.resize((int(new_x), int(new_y))).save('end.jpg')


if __name__ == '__main__':
	iphone5_size = [1136, 640]
	shape_pic_size("001.jpg", iphone5_size)


