#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：StudentInfoInput.py
@Author ：zhangyi
@Date ：2022/5/27 9:08 AM
'''
import json
from typing import Dict, List
from HttpRequest.HttpRequest import HttpRequest
import yaml

"""
前端学生录入信息
"""


class StudentInfoInput:
	def __init__(
			self,
	):
		self.env = 'dev'
		self.config = self.load_config()
		self.headers = self.config['base']['headers']
		self.requestParamsForSetupOne = self.config['setupOne']['params']
		self.requestParamsForSetupTwo = self.config['setupTwo']['params']
		self.requestParamsForSetupThree = self.config['setupThree']['params']
		self.token = None
		self.get_token()

	"""
	class方法，加载配置文件
	"""

	@classmethod
	def load_config(
			cls,
	):
		with open('config.yaml', 'r') as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
			return data

	@staticmethod
	def assertReturnResult(reponseJson):
		if reponseJson['status'] != 200:
			print("服务器返回错误，程序退出，请联系研发！")
			exit(123)

	"""
	设置环境
	"""

	def set_env(
			self,
			env: str
	) -> None:
		self.env = env

	"""
	设置headers
	"""

	def set_headers(
			self,
			headers: Dict
	) -> None:
		self.headers = headers

	"""
	用户登录,获取用户token
	"""

	def get_token(
			self,
	) -> None:
		config = self.load_config()
		t = HttpRequest(config['env'][self.env]['requestDomain'] + config['login']['requestPath'])
		t.set_header(self.headers)
		t.set_params({
			'phone': self.config['login']['phone'],
			'password': self.config['login']['password']
		})
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		self.assertReturnResult(reponseJson)
		self.token = reponseJson['result']['token']

	"""
	获取学校id
	"""

	def get_school_id(self):
		schoolName = self.config['setupOne']['params']['schoolName']
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['getSchoolIDWriteConfig']['requestPath'])
		t.set_params({
			'fuzzyWords': schoolName,
		})
		self.headers['t'] = self.token
		t.set_header(self.headers)
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		self.assertReturnResult(reponseJson)
		return reponseJson['result'][0]['id']

	"""
	获取行业id列表
	"""

	def get_industry_list_id(
			self,
	):
		industry_list_name = self.config['setupTwo']['params']['industryIds']
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['industryList']['requestPath'])
		print(self.config['env'][self.env]['requestDomain'] + self.config['industryList']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		self.assertReturnResult(reponseJson)
		insustry_id_list = list()
		for insustry_name in industry_list_name:
			for industry_info in reponseJson['result']:
				if insustry_name == industry_info['industryName']:
					insustry_id_list.append(industry_info['id'])
		print(insustry_id_list)
		return insustry_id_list

	"""
	意向职位id查询
	"""

	def get_intended_positions(
			self,
	):
		intendedPositionsList = self.config['setupTwo']['params']['postIds']
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['intendedPositionId']['requestPath'])
		t.set_params({
			'intendedPositionsList': intendedPositionsList,
		})

	"""
	获取意向职能列表
	"""

	def get_functions_id_list(
			self,
	) -> List:
		functions_name_list = self.config['setupTwo']['params']['functions']
		print(functions_name_list)
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['functionList']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		self.assertReturnResult(reponseJson)
		functions_list = list()
		for x in functions_name_list:
			for y in reponseJson['result']:
				print(y)
				if x['functionName'] == y['functionName']:
					for z in x['children']:
						for i in y['children']:
							if z['functionName'] == i['functionName']:
								id_list = []
								id_list.append(y['functionId'])
								id_list.append(i['functionId'])
								functions_list.append(id_list)
		return functions_list

	"""
	工作区域列表
	"""

	def get_expected_areas_code_list(
			self
	) -> List:
		expectedAreasNameeList = self.config['setupTwo']['params']['expectedAreas']
		areasList = list()
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['expectedAreasCodeList']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		t.set_params({
			'id': 1
		})
		reponseAllObject = t.send_http_request(method='get')
		reponseAllJson = t.analysis_reponse_json_data(reponseAllObject)
		self.assertReturnResult(reponseAllJson)
		for x in expectedAreasNameeList:
			print(x)
			for y in reponseAllJson['result']:
				print(y)
				if x['area'] == y['name']:
					t.set_params(
						{
							'id': y['id']
						}
					)
					reponseObject = t.send_http_request(method='get')
					reponseJson = t.analysis_reponse_json_data(reponseObject)
					self.assertReturnResult(reponseJson)
					for i in reponseJson['result']:
						print(i)
						codeList = []
						for z in x['childAreas']:
							if i['name'] == z['name']:
								codeList.append(y['code'])
								codeList.append(i['code'])
								areasList.append(codeList)
		return areasList

	"""
	未来可迁移区域列表
	"""

	def get_future_areas_code_list(
			self
	) -> List:
		expectedAreasNameeList = self.config['setupTwo']['params']['futureAreas']
		areasList = list()
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['expectedAreasCodeList']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		t.set_params({
			'id': 1
		})
		reponseAllObject = t.send_http_request(method='get')
		reponseAllJson = t.analysis_reponse_json_data(reponseAllObject)
		self.assertReturnResult(reponseAllJson)
		for x in expectedAreasNameeList:
			print(x)
			for y in reponseAllJson['result']:
				print(y)
				if x['area'] == y['name']:
					t.set_params(
						{
							'id': y['id']
						}
					)
					reponseObject = t.send_http_request(method='get')
					reponseJson = t.analysis_reponse_json_data(reponseObject)
					self.assertReturnResult(reponseJson)
					for i in reponseJson['result']:
						codeList = []
						for z in x['childAreas']:
							if i['name'] == z['name']:
								codeList.append(y['code'])
								codeList.append(i['code'])
								areasList.append(codeList)
		return areasList

	"""
	获取一级学科id列表
	"""

	def get_subject_info(
			self,
	) -> List:
		subjectInfoName = self.requestParamsForSetupThree['subjectId']['subjectName']['name']
		subjectInfoChildrenName = self.requestParamsForSetupThree['subjectId']['subjectName']['children']
		layer = 2
		type = self.requestParamsForSetupThree['schoolType']
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['subjectInfo']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		t.set_params({
			'layer': layer,
			'type': type
		})
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		print(reponseJson)
		subjectIdList = list()
		self.assertReturnResult(reponseJson)

		for x in reponseJson['result']:
			if subjectInfoName == x['name']:
				for y in x['children']:
					if subjectInfoChildrenName == y['name']:
						print(x['name'])
						idList = []
						idList.append(x['id'])
						idList.append(y['id'])
						subjectIdList.append(idList)
		return subjectIdList

	"""
	获取专业id列表
	"""

	def get_professionSubject_info(
			self,
	) -> List:
		subjectInfoName = self.requestParamsForSetupThree['professionSubjectId']['subjectName']['name']
		subjectInfoChildrenName = \
		self.requestParamsForSetupThree['professionSubjectId']['subjectName']['subjectchildren']['name']
		subjectInfoChildrenNameChildren = \
		self.requestParamsForSetupThree['professionSubjectId']['subjectName']['subjectchildren']['children']
		layer = 3
		type = self.requestParamsForSetupThree['schoolType']
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['subjectInfo']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		t.set_params({
			'layer': layer,
			'type': type
		})
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		print(reponseJson)
		subjectIdList = list()
		self.assertReturnResult(reponseJson)
		for x in reponseJson['result']:
			if subjectInfoName == x['name']:
				for y in x['children']:
					if subjectInfoChildrenName == y['name']:
						for z in y['children']:
							idList = []
							idList.append(x['id'])
							idList.append(y['id'])
							idList.append(z['id'])
							subjectIdList.append(idList)
		return subjectIdList

	def get_like_subject_info(
			self,
	) -> List:
		subjectInfoName = self.requestParamsForSetupThree['likeSubjectIds']['subjectName']['name']
		subjectInfoChildrenName = self.requestParamsForSetupThree['likeSubjectIds']['subjectName']['subjectchildren'][
			'name']
		subjectInfoChildrenNameChildren = \
		self.requestParamsForSetupThree['likeSubjectIds']['subjectName']['subjectchildren']['children']
		layer = 3
		type = self.requestParamsForSetupThree['schoolType']
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['subjectInfo']['requestPath'])
		self.headers['t'] = self.token
		t.set_header(self.headers)
		t.set_params({
			'layer': layer,
			'type': type
		})
		reponseObject = t.send_http_request(method='get')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		print(reponseJson)
		subjectIdList = list()
		self.assertReturnResult(reponseJson)
		for x in reponseJson['result']:
			if subjectInfoName == x['name']:
				for y in x['children']:
					if subjectInfoChildrenName == y['name']:
						for z in y['children']:
							idList = []
							idList.append(x['id'])
							idList.append(y['id'])
							idList.append(z['id'])
							subjectIdList.append(idList)
		return subjectIdList

	"""
	求职基本信息录入
	"""

	def setup_one(
			self,
	):
		requestParams = self.requestParamsForSetupOne
		requestParams['schoolId'] = self.get_school_id()
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['setupOne']['requestPath'])
		t.set_data(json.dumps(requestParams))
		self.headers['t'] = self.token
		t.set_header(self.headers)
		reponseObject = t.send_http_request(method='post')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		return reponseJson

	"""
	求职意向信息录入
	"""

	def setup_two(
			self,
	):
		requestParams = self.requestParamsForSetupTwo
		requestParams['industryIds'] = self.get_industry_list_id()
		requestParams['functions'] = self.get_functions_id_list()
		requestParams['expectedAreas'] = self.get_expected_areas_code_list()
		requestParams['futureAreas'] = self.get_future_areas_code_list()
		t = HttpRequest(
			self.config['env'][self.env]['requestDomain'] + self.config['setupTwo']['requestPath'])
		t.set_data(json.dumps(requestParams))
		self.headers['t'] = self.token
		t.set_header(self.headers)
		reponseObject = t.send_http_request(method='post')
		reponseJson = t.analysis_reponse_json_data(reponseObject)
		return reponseJson

	def setup_three(
			self
	):
		pass


s = StudentInfoInput()
s.set_env('dev')
s.get_professionSubject_info()
