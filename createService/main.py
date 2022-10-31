#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：main.py
@Author ：zhangyi
@Date ：2022/5/18 10:10 AM
'''
from JenkinsTaskForJob import JenkinsTaskForJob
from AliyunImageRepositoryManage import AliyunImageRepositoryManage
if __name__ == '__main__':
	env = "pro"
	service_type = 'front'
	service_name = "provider-b-career-recruit"
	jenkins_job = JenkinsTaskForJob(env,service_type,service_name)
	jenkins_job.create_service_job_for_jenkins()
	# aliyun_image_object = AliyunImageRepositoryManage(env,service_type,service_name)
	# aliyun_image_object.create_image_repository()
