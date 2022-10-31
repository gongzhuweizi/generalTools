#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：AliyunImageRepositoryManage.py
@Author ：zhangyi
@Date ：2022/5/25 1:27 PM
'''
from Api.AliyunImageApi import AliyunImageApi
from Tools import tools

"""
阿里云镜像仓库管理类
"""
class AliyunImageRepositoryManage:
	def __init__(
			self,
			env: str,
			service_type: str,
			service_name: str
	):
		"""

		@param env:
		@param service_type:
		@param service_name:
		"""
		self.env = env
		self.service_type = service_type
		self.service_name = service_name
	"""
	创建镜像曾库
	"""
	def create_image_repository(
			self
	) -> None:
		image_params_config_base = tools.get_yaml_object('Config/env.yaml')['env'][self.env]['image'] #获取环境中最基本配置
		access_key_id = image_params_config_base['access_key_id'] #阿里云key
		access_key_secret = image_params_config_base['access_key_secret'] #阿里云secret
		config_endpoint = image_params_config_base['config_endpoint'] #阿里云endpoint
		instance_id = image_params_config_base['instance_id'] #实例id
		repo_name = self.env + '_' + self.service_type + '_' + self.service_name #仓库名称
		repo_namespace_name = "wx-wm-"+self.env #命名空间
		image_front_xml_params = dict()
		if self.service_type == "front":
			image_front_xml_params = tools.get_yaml_object('Config/front_service_config.yaml')['image']
		elif self.service_type == "backend":
			image_front_xml_params = tools.get_yaml_object('Config/backend_service_config.yaml')['image']
		summary = image_front_xml_params['summary']  #镜像仓库注解
		detail = image_front_xml_params['detail'] #镜像仓库描述
		#获取阿里云api
		aliyun_image_object = AliyunImageApi(
			access_key_id=access_key_id,
			access_key_secret=access_key_secret,
			config_endpoint=config_endpoint
		)
		#创建镜像仓库
		aliyun_image_object.create_aliyun_image_repository(
			instance_id,
			repo_name,
			repo_namespace_name,
			summary,
			detail)
