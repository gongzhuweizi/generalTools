#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：JenkinsAuth.py
@Author ：zhangyi
@Date ：2022/4/15 11:32 AM
'''

from dataclasses import dataclass


@dataclass
class JenkinsAuth:
	server_url: str
	username: str
	password: str
	token: str

