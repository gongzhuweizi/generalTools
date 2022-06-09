#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：JenkinsApi.py
@Author ：zhangyi
@Date ：2022/4/15 11:20 AM
'''
import jenkins

"""
"""


class JenkinsApi:
	def __init__(
			self,
			server_url: str,
			user: str,
			token: str
	):
		self.server_url = server_url
		self.user = user
		self.token = token
		self.conn = jenkins.Jenkins(self.server_url, username=self.user, password=self.token)

