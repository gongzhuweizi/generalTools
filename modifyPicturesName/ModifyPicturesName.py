#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：ModifyPicturesName.py
@Author ：zhangyi
@Date ：2022/2/28 6:54 PM
'''
import os
import re
"""
批量修改单个文件夹下的文件名称
"""
class ModifyPicturesName():
	def __init__(self):
		pass
	"""
	设置需要修改的文件所在目录
	"""
	def set_picture_dir(
		self,
		picture_dir : str
	) ->object:
		"""
		@param picture_dir: str
		"""
		self.picture_dir = picture_dir
	"""
	获取需要修改的文件所在目录
	"""
	def get_pictures_dir(
			self
	) -> str :
		"""
		@rtype: str
		"""
		return self.picture_dir
	"""
	判断是否为文件、目录是否存在
	"""
	def pictures_dir_exist(
			self
	) -> bool :
		"""

		@rtype: bool
		"""
		if os.path.isfile(self.picture_dir):
			print("\033[4;31m输入的是文件，非目录\033[0m")
			return False
		elif os.path.isdir(self.picture_dir):
			return True
		else:
			print("\033[4;31m目录不存在！请重新输入！\033[0m")
			return False
	"""
	配置文件前缀
	"""
	def set_file_befor(
			self,
			file_befor : str
	) -> object :
		"""
		@param file_befor:  str
		"""
		self.file_befor = file_befor
	"""
	获取文件前缀名称
	"""
	def get_file_befor_name(
			self
	) -> str :
		"""

		@rtype: str
		"""
		return self.file_befor
	"""
	解析文件前缀名称
	"""
	def analysis_file_befor_name(
			self
	) -> bool :
		"""

		@rtype: bool
		"""
		if "*" in self.file_befor:
			return True
		else:
			print("\033[4;31m输入的文件名不包含*号!\033[0m")
			return False
	"""
	获取目录内的文件名称与目录对应字典
	"""
	def get_dir_file_name(
			self
	) -> dict :
		"""
		@rtype: dict
		"""
		file_dict = {}
		file_object = os.walk(self.picture_dir)
		for root, dirs, files in file_object:
			for x in files:
				if x.startswith('.'):
					continue
				file_dict[x] = root
		if len(file_dict.keys()) <= 0:
			print("\033[4;31目录内文件为空！\033[0m")
			return False
		return file_dict
	"""
	文件数量的位数
	"""
	def get_dir_file_count_digit(
			self,
			picture_dir : str
	) -> int:
		"""

		@rtype: int
		"""
		path_file_number = len(str(len((os.listdir(picture_dir)))))
		if path_file_number == 1:
			path_file_number ==2
			return 2
		return path_file_number

"""
主函数
"""
if __name__ == '__main__':
	"""
	主函数入口
	"""
	while True:
		picture_dir = input("\033[33m请输入需要改名文件所在的目录:\n\033[0m")
		m = ModifyPicturesName()  # 初始化类实例
		m.set_picture_dir(picture_dir)  # 设置图片所在目录
		# 获取图片数量位数，例如24个图片，位数为2
		dir_exist = m.pictures_dir_exist()
		if not dir_exist:  # 如果不存在提示重新输入
			continue
		# 判断是否存在
		file_dict = m.get_dir_file_name()
		if file_dict == False:
			continue
		while True:
			path_file_number = m.get_dir_file_count_digit(picture_dir)
			picture_file_name = input("\033[33m请输入文件前缀名称:\n\033[0m") #配置文件名称
			m.set_file_befor(picture_file_name) #配置图片前缀

			if m.analysis_file_befor_name(): #解析图片前缀名字是否合法，不合法继续输入
				file_list_keys  = sorted([ x for x in file_dict.keys()]) #获取所有的文件名称
				modify_secuess = 0
				modify_fail = 0
				for x in file_list_keys : #遍历所有文件名
					old_file = x
					#把所有文件名称改为新文件名
					new_filename = re.sub(r'\*+', str(file_list_keys.index(x)+1).zfill(path_file_number), picture_file_name)
					#调用修改文件方法
					try:
						os.rename(file_dict[x]+"/"+old_file,file_dict[x]+"/"+new_filename)
						print("\033[32m源目录文件:\033[0m"+file_dict[x]+"/"+old_file+"----> 目的文件："+file_dict[x]+"/"+new_filename+"  "+"修改成功！")
						modify_secuess = modify_secuess + 1
					except Exception as e:
						modify_fail = modify_fail + 1
						print("\033[4;31m源目录文件:\033[0m"+file_dict[x]+"/"+old_file+"----> 目的文件："+file_dict[x]+"/"+new_filename+"  "+"修改失败！"+e)
				print("\033[33m文件总数为:\033[0m"+str(len(file_list_keys))+",\033[32m文件修改成功个数为:\033[0m"+str(modify_secuess)+",\033[031m失败个数为:\033[0m"+str(modify_fail)+".")
			else:
				continue
			break
		break








