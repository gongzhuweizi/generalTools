#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：AliyunBaseApi.py
@Author ：zhangyi
@Date ：2022/5/25 1:22 PM
'''
from alibabacloud_cr20181201.client import Client as cr20181201Client
from alibabacloud_tea_openapi import models as open_api_models
class AliyunBaseApi:
    def __init__(
            self,
            access_key_id: str,
            access_key_secret: str,
            config_endpoint :str
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.config_endpoint = config_endpoint
    def create_client(
            self

    ) -> cr20181201Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=self.access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=self.access_key_secret
        )
        # 访问的域名
        config.endpoint = self.config_endpoint
        return cr20181201Client(config)
