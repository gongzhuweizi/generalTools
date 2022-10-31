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
	default_git_branch: str
	project_name: str
	service_name: str
	deployment_env: str
	service_port: str
	git_url: str
	git_redentials: str
	ssh_host: str
