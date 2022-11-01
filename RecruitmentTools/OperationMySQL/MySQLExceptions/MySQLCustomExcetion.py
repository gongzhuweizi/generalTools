# -*-coding:utf-8 -*-
"""
@Author: zhangyi
@Time: 2021/12/31 11:33 上午
@File: MySQLCustomExcetion.py
@IDE: PyCharm
"""
class MySQlSqlNullExcetion(Exception):
	def __init__(
			self,
			messages :str
	):
		self.messages = messages
	def __str__(self):
		return self.messages



