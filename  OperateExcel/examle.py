# -*-coding:utf-8 -*-
"""
@Author: zhangyi
@Time: 2021/7/26 3:47 下午
@File: examle.py
@IDE: PyCharm
"""
import pandas as pd
from OperateExcel import OperateExcel
from Tools import fileExsits

if __name__ == '__main__':
	"""
	添加sheet
	"""
	def test6():
		op = OperateExcel()
		op.setSheetName("哈哈哈")
		op.setExcelDirFileName("excelData/demo-2021-07-26.xlsx")
		data = [['a','b']]
		op.setExcelColumns(['标题列1','标题列2'])
		op.setExcelData(data)
		op.addExcelSheetWrite()
	test6()

    # """
	# 按照行写入
	# """
	# def test2():
	# 	op = OperateExcel()
	# 	columns=['col 1', 'col 2']
	# 	op.setExcelColumns(columns)
	# 	data = [['a', 'b'], ['c', 'd']]
	# 	op.setSheetName("孩子")
	# 	op.setExcelData(data)
	# 	op.pdLineListWrite()
	# test2()
	# """
	# 按照列进行写入
	# """
	# def test3():
	# 	op = OperateExcel()
	# 	data = {'标题列1': ['张三','李四'],
	# 			'标题列2': [80, 90]
	# 			}
	# 	op.setSheetName("孩子")
	# 	op.setExcelData(data)
	# 	op.pdColumnDictWrite()
	# test3()
	# """
	# 按照行追加写入
	# """
	# def test4():
	# 	op = OperateExcel()
	# 	data = [['a','b']]
	# 	op.setSheetName("孩子")
	# 	op.setExcelHeaders(True)
	# 	op.setExcelColumns(['标题列1','标题列2'])
	# 	op.setExcelData(data)
	# 	op.pdAppendListWrite()
	#
	# test4()
	# """
	# 读取excel
	# """
	# def test5():
	# 	op = OperateExcel()
	# 	d = op.readExcelFileName()
	# 	print(type(d))
	# test5()











