# 每个人都是普通人，我也是，如果不写这个文档的话，每次隔几天再看这些文件自己就会发蒙，
# 如果写了这些文档，就可以顺着这些笔记，找回思路，迅速上手。
文件：
getAllEducation.py:
	下载profile表中的所有未下载教育信息的微博用户
getAllProfile.py:
	下载特定学校微博用户中的那些未下载关注列表的（is_profile=-1）人的关注列表，存储到profile表中
	注：每次需要改动学校名称
getAllSchool.py:
	将education中属于某个特定学校的用户id插入到对应的学校表中
	注：每次需要改动学校名称
getAllWeibos.py
	下载某个学校未下载微博的用户的微博
	注：每次需要改动学校名称
	依赖：wb_ori_no_pic.py
wb_ori_no_pic.py:
	封装一个学校的微博访问数据。
	注：每次需要改动学校名称