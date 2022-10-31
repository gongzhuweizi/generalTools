#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：JenkinsTaskForJob.py
@Author ：zhangyi
@Date ：2022/5/18 10:12 AM
'''
from typing import List

from Tools import tools
from Api import JenkinsApi

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
		self.jenkins_job_config = self.env_params_config['env'][self.env]
		self.jenkins_username = self.jenkins_job_config['jenkins']['username']
		self.jenkins_token = self.jenkins_job_config['jenkins']['token']
		self.jenkins_host = self.jenkins_job_config['jenkins'][self.service_type]['host']
		self.jenkins_git_branch = self.jenkins_job_config['jenkins']['git']['default_branch']
		self.jenkins_git_credentials_id = self.jenkins_job_config['jenkins']['git']['credentials_id']

	"""
	创建jenkins任务
	"""

	def create_service_job_for_jenkins(
			self
	):
		"""
		@param service_type:
		@param env:
		@param jenkins_params_config:
		@param service_full_name:
		"""
		job_name = self.env + '_' + self.service_type + '_' + self.service_name  # 任务名称
		jenkins_view = self.jenkins_job_config['jenkins'][self.service_type]['view']  # 任务视图
		jenkins_server_url = self.jenkins_host + jenkins_view  # 服务url=jenkins主机地址+任务视图
		# 根据环境配置jenkinsxml文件环境参数和服务名称参数
		jenkins_job_xml_params_list = \
			[
				{"tag_name": "string", "template_project_text": "env", "new_project_text": self.env},
				{"tag_name": "string", "template_project_text": "front_service_name",
				 "new_project_text": self.service_name},
				{"tag_name": "defaultValue", "template_project_text": "default_branch",
				 "new_project_text": self.jenkins_git_branch},
				{"tag_name": "credentialsId", "template_project_text": "credentialsId",
				 "new_project_text": self.jenkins_git_credentials_id},
			]
		jenkins_job_xml_template = ''  # 默认的job模板路径，
		if self.service_type == "front":  # 如果服务是前端服务，则找front.xml，并把环境和服务名称添加到模板list中
			jenkins_job_xml_template = 'JenkinsTemplate/front.xml'
			jenkins_front_job_xml_params_list = tools.get_yaml_object('Config/front_service_config.yaml')['jenkins']
			for x in jenkins_front_job_xml_params_list:
				jenkins_job_xml_params_list.append(x)

		elif self.service_type == "backend":  # 如果服务是后端服务，则找backend.xml，并把环境和服务名称添加到模板list中
			jenkins_job_xml_template = 'JenkinsTemplate/backend.xml'
			jenkins_backend_job_xml_params_list = tools.get_yaml_object('Config/backend_service_config.yaml')['jenkins']
			for x in jenkins_backend_job_xml_params_list:
				jenkins_job_xml_params_list.append(x)
		else:
			print("错误，服务类型错误")
			exit(127)
		# 获取jenkins连接
		jenkins_api = JenkinsApi.JenkinsApi(
			server_url=jenkins_server_url,
			username=self.jenkins_username,
			token=self.jenkins_token
		)
		dom = tools.update__xml(jenkins_job_xml_template, jenkins_job_xml_params_list)  # 把模板文件更新成新的服务配置文件
		jenkins_job_service_xmlpath = job_name + '.xml'  # 新的模板文件名称
		fp = open(jenkins_job_service_xmlpath, 'w', encoding='utf-8')
		dom.writexml(fp, indent='', addindent='', newl='', encoding='utf-8')
		fp.close()
		service_config = tools.get_xml_object(jenkins_job_service_xmlpath)  # 获取新的xml配置文件
		jenkins_api.create_job(service_config, job_name)  # 创建任务

	""""
	构建job
	"""

	def build_service_job_for_jenkins(self):
		pass
