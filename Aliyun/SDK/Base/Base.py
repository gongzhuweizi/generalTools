from typing import List
from alibabacloud_cr20181201.client import Client as cr20181201Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cr20181201 import models as cr_20181201_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
class Base:
	def __init__(self,
				 access_key_id: str,
				 access_key_secret: str,
				 endpoint: str
				 ):
		self.access_key_id = access_key_id
		self.access_key_secret = access_key_secret
		self.endpoint = endpoint

	def create_client(
			self,
	) -> cr20181201Client:
		"""
		使用AK&SK初始化账号Client
		@param access_key_id:
		@param access_key_secret:
		@return: Client
		@throws Exception
		"""
		config = open_api_models.Config(
			# 您的 AccessKey ID,
			access_key_id=self.access_key_id,
			# 您的 AccessKey Secret,
			access_key_secret=self.access_key_secret
		)
		# 访问的域名
		config.endpoint = self.endpoint
		return cr20181201Client(config)
