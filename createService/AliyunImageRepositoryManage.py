#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：AliyunImageRepository.py
@Author ：zhangyi
@Date ：2022/5/25 1:27 PM
'''
from Api.AliyunImageApi import AliyunImageApi
class CreateAliyunImageRepository:
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
	def create_image_repository(self):
		aliyun_image_object = AliyunImageApi()
		aliyun_image_object.create_aliyun_image_repository(

		)



