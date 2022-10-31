#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：tools.py
@Author ：zhangyi
@Date ：2022/5/18 9:53 AM
'''
from typing import Any
import yaml
import xml.dom.minidom

"""
解析yaml文件，返回一个yaml object
"""


def get_yaml_object(
		yaml_dir: str
) -> Any:
	"""
	@param yaml_dir:
	@return: Any
	"""
	with open(yaml_dir, 'r') as f:
		data = yaml.load(f, Loader=yaml.FullLoader)
		return data


"""
返回一个xml object
"""


def get_xml_object(
		template
) -> str:
	"""

	@param template: str
	@return: str
	"""
	with open(template, 'r') as f:
		return f.read()


"""
根据xml标签定位元素，并更新数值
"""


def update__xml(
		xml_template,
		xml_params_list
) -> xml.dom.minidom:
	"""

	@param xml_template: str
	@param xml_params_list: str
	@return: xml.dom.minidom
	"""
	dom = xml.dom.minidom.parse(xml_template)
	for x in xml_params_list:
		tag_elements = dom.getElementsByTagName(x['tag_name'])
		for element in tag_elements:
			if element.firstChild.data == x['template_project_text']:
				element.firstChild.data = x['new_project_text']
	return dom
