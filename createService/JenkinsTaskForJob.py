#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：CreateJenkinsJob.py
@Author ：zhangyi
@Date ：2022/5/18 10:12 AM
'''
from typing import List

from Tools import tools
from Api import jenkinsApi

"""
jenkins操作类,初始化三个属性
jenkins_host:主机地址
jenkins_username: jenkins用户名
jenkins_token: jenkins token
"""


class JenkinsTaskForJob:
	def __init__(
			self,
			env: str,
			service_type: str,
			service_name: str
	):
		"""

		@param jenkins_host:
		@param jenkins_username:
		@param jenkins_token:
		"""
		self.env = env
		self.service_type = service_type
		self.service_name = service_name
		self.env_params_config = tools.get_yaml_object('Config/env.yaml')
		print(self.env_params_config)
		self.jenkins_job_config = self.env_params_config['env'][self.env]
		self.jenkins_username = self.jenkins_job_config['jenkins']['username']
		self.jenkins_token = self.jenkins_job_config['jenkins']['token']
		self.jenkins_host = self.jenkins_job_config['jenkins'][self.service_type]['host']

	def create_service_job_for_jenkins(
			self,


	):
		"""
		@param service_type:
		@param env:
		@param jenkins_params_config:
		@param service_full_name:
		"""
		service_full_name = self.env + '_' + self.service_type + '_' + self.service_name
		jenkins_view = self.jenkins_job_config['jenkins'][self.service_type]['view']
		jenkins_server_url = self.jenkins_host + jenkins_view
		jenkins_job_xml_params_list = [{"tag_name": "string", "template_project_text": "env", "new_project_text": self.env},
									   {"tag_name": "string", "template_project_text": "front_service_name",
										"new_project_text": self.service_name}]
		jenkins_job_xml_template = ''
		if self.service_type == "front":
			jenkins_job_xml_template = 'JenkinsTemplate/front.xml'
			jenkins_front_job_xml_params_list = tools.get_yaml_object('Config/front_update_jenkins_config.yaml')
			for x in jenkins_front_job_xml_params_list:
				jenkins_job_xml_params_list.append(x)

		elif self.service_type == "backend":
			jenkins_job_xml_template = 'JenkinsTemplate/backend.xml'
			jenkins_backend_job_xml_params_list = tools.get_yaml_object('Config/backend_update_jenkins_config.yaml')
			for x in jenkins_backend_job_xml_params_list:
				jenkins_job_xml_params_list.append(x)
		else:
			print("错误，服务类型错误")
			exit(127)

		jenkins_api = jenkinsApi.JenkinsApi(
			server_url=jenkins_server_url,
			username=self.jenkins_username,
			token=self.jenkins_token
		)
		dom = tools.update__xml(jenkins_job_xml_template, jenkins_job_xml_params_list)
		jenkins_job_service_xmlpath = service_full_name + '.xml'
		fp = open(jenkins_job_service_xmlpath, 'w', encoding='utf-8')
		dom.writexml(fp, indent='', addindent='', newl='', encoding='utf-8')
		fp.close()
		service_config = tools.get_xml_object(jenkins_job_service_xmlpath)
		jenkins_api.create_job(service_config, service_full_name)

	def build_service_job_for_jenkins(self):
		pass



