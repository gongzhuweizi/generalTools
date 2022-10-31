#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：JenkinsApi.py
@Author ：zhangyi
@Date ：2022/4/15 11:20 AM
'''
import jenkins
from DataClass import JenkinsAuth

"""
"""


class JenkinsApi:
	def __init__(
			self,
			JenkinsAuth: JenkinsAuth,
	):
		self.JenkinsAuth = JenkinsAuth
	def analysis_jenkins_template(self):
		pass
	def create_job_for_template(self):
		pass



