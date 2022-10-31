#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：XmlAnalysis.py
@Author ：zhangyi
@Date ：2022/4/15 4:16 PM
'''
try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET
from typing import Union


# t = tree.getroot()
# x = t.iter('net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition')
# for i in x:
# 	print(i[0].text)

class AnalysisXml:
	"""
	构造函数
	"""

	def __init__(
			self,
			xml_path: str
	):
		self.xml_path = xml_path

	"""
	设置xml文件路径
	"""

	def set_xml_path(
			self,
			xml_path: str
	):
		"""

		@param xml_path: str
		"""
		self.xml_path = xml_path

	"""
	获取xml对象
	"""

	def __get_xml_object(
			self
	) -> ET:
		"""

		@rtype: ET
		"""
		return ET.parse(self.xml_path)

	"""
	获取根元素对象
	"""

	def __get_xml_root(
			self
	) -> ET:
		"""

		@rtype: ET
		"""
		return self.__get_xml_object().getroot()

	"""
	获取节点元素，传入节点标签
	"""
	def get_xml_xpath(self,xpath):
		xml_object = self.__get_xml_object()
		obj = []
		for x in xml_object.iterfind(xpath):
			obj.append(x)
		if len(obj) > 1:
			exit(123)
		return obj[0].text



a = AnalysisXml('../JenkinsJobTemplate/Spring.xml')
cmd = a. get_xml_xpath('')

print(cmd)




