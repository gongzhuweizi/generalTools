#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：AliyunImageApi.py
@Author ：zhangyi
@Date ：2022/5/18 12:03 PM
'''
from Api.AliyunBaseApi import AliyunBaseApi
from alibabacloud_cr20181201 import models as cr_20181201_models
from alibabacloud_tea_util import models as util_models


class AliyunImageApi(AliyunBaseApi):
	def __init__(
			     self,
				 access_key_id: str,
				 access_key_secret: str,
				 config_endpoint: str
	):
		super().__init__(
			access_key_id,
			access_key_secret,
			config_endpoint
		)
		self.repo_type = 'PRIVATE'
	def set_repo_type(self,
					  repo_type
	):
		self.repo_type = repo_type
	def get_repo_type(
			self
	):
		return self.repo_type
	def create_aliyun_image_repository(
			self,
			instance_id: str,
			repo_name: str,
			repo_namespace_name: str,
			summary: str,
			detail: str

	) -> None:
		"""

		@param instance_id:
		@param repo_name:
		@param repo_namespace_name:
		@param repo_type:
		@param summary:
		@param detail:
		"""
		client = self.create_client()
		create_repository_request = cr_20181201_models.CreateRepositoryRequest(
			instance_id=instance_id,
			repo_name=repo_name,
			repo_namespace_name=repo_namespace_name,
			repo_type=self.repo_type,
			summary=summary,
			detail=detail
		)
		runtime = util_models.RuntimeOptions()
		# 复制代码运行请自行打印 API 的返回值
		print(client.create_repository_with_options(create_repository_request, runtime))
