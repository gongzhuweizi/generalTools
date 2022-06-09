#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：jenkins.py
@Author ：zhangyi
@Date ：2022/5/18 9:53 AM
'''
import yaml
def get_yaml_object(yaml_dir):
	with open(yaml_dir, 'r') as f:
		data = yaml.load(f)
		return  data


