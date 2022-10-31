#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：JenkinsApi.py
@Author ：zhangyi
@Date ：2022/5/17 1:35 PM
'''

import jenkins

"""
jenkins 操作类
"""


class JenkinsApi:
	def __init__(
			self,
			server_url=None,
			username=None,
			token=None
	):
		"""

		@param server_url:
		@param username:
		@param token:
		"""
		self.server_url = server_url
		self.user = username
		self.token = token
		self.server = jenkins.Jenkins(self.server_url, self.user, self.token)  # 创建一个jenkins server

	"""
	获取一个job
	"""

	def get_jenkins_job_info(
			self,
			job_name: str

	) -> jenkins.Jenkins:
		"""

		@param job_name: str
		@return: jenkins.Jenkins
		"""
		job_info = self.server.reconfig_job(job_name)
		return job_info

	"""
	创建job
	"""

	def create_job(
			self,
			service_config: str,
			job_name: str
	) -> None:
		"""
		@param service_config: str
		@param job_name: str
		"""
		server = self.server
		try:
			server.create_job(job_name, config_xml=service_config)
		except jenkins.JenkinsException as e:
			print("任务创建不成功！任务已经存在！请检查！")
			exit(127)
