# -*-coding:utf-8 -*-
"""
@Author: zhangyi
@Time: 2021/7/12 2:43 下午
@File: Tools.py
@IDE: PyCharm
"""

import datetime
import os
def getCurrentTimeYMD():
	return datetime.datetime.now().strftime('%Y-%m-%d')
def fileExsits(filename):
	if not os.path.exists(filename):
		return False
	else:
		return True




