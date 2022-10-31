#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：StudentInfoInputbak.py
@Author ：zhangyi
@Date ：2022/5/31 9:31 AM
'''
import asyncio
import time
from typing import Dict, List
import aiohttp
import yaml
import json

""""
异步http请求封装类
"""


class AsyncHttpTask():
	"""
	初始化传入url列表
	"""

	def __init__(
			self,

	):
		self.__requestMethod = str  # 定义请求方法
		self.__requestParams = dict()  # 定义get请求参数
		self.__requestData = dict()  # 定义post请求参数
		self.__requestHeaders = dict()  # 定义请求header
		self.requestLimit = int  # 定义任务并发数
		self.config = self.load_config()  # 加载配置文件
		self.__requestMaxTask = int  # 最大任务数量
		self.env = 'dev'  # 请求环境，默认为dev
		self.requestSleep = 0

	"""
	静态方法，判断返回结果
	"""

	@staticmethod
	def assertReponseResultCode(reponseJson):
		if reponseJson['status'] != 200:
			print("服务器返回错误，程序退出，请联系研发！")
			exit(123)

	"""
	静态方法，加载请求配置文件
	"""

	@classmethod
	def load_config(
			cls,
	) -> Dict:
		with open('config.yaml', 'r') as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
			return data
	"""
	设置延迟请求http
	"""
	def set_request_sleep(
			self,
			requestSleep
	):
		self.requestSleep = requestSleep

	"""
	异步发送http请求方法
	"""

	async def send_http_request(
			self
	):
		pass

	"""
	配置环境  dev alpha beta pro
	"""

	def set_request_env(
			self,
			env
	):
		self.env = env

	"""
	配置请求方法
	"""

	def set_request_method(
			self,
			requestMethod: str
	):
		self.__requestMethod = requestMethod

	"""
	配置get请求参数
	"""

	def set_request_params(
			self,
			requestParams: Dict
	):
		self.__requestParams = requestParams

	"""
	配置post请求参数
	"""

	def set_request_data(
			self,
			requestData: Dict
	):
		self.__requestData = requestData

	"""
	配置请求最大任务并发数
	"""

	def set_request_max_task(
			self,
			requestMaxTask: int
	):
		self.__requestMaxTask = requestMaxTask

	"""
	配置请求header头
	"""

	def set_request_headers(
			self,
			requestHeaders: Dict
	):
		self.__requestHeaders = requestHeaders

	def set_request_task_limit(
			self,
			requestLimit: int
	):
		self.__requestLimit = requestLimit

	"""
	获取token异步任务，token会存放在队列中，相当于生产者
	"""

	async def async_get_token_task(
			self,
			userLoginUrl: str,
			userLoginParams: Dict, # 传入一个队列，token会存放在队列里面# 传入访问的接口地址
			requestLimit: int,  # 传入任务并发数量
			taskQueue: asyncio.queues.Queue(),
	):
		async with requestLimit:
			async with aiohttp.ClientSession() as session:  # 使用异步http请求
				self.set_request_headers(self.config['base']['headers'])# 从配置文件获取headers

				async with session.get(userLoginUrl, headers=self.__requestHeaders,
									   params=userLoginParams) as response:  # 发送异步请求
					reponseJson = await response.json()# 异步请求获取json数据
					# self.assertReponseResultCode(reponseJson)  # 判断json结果
					print(reponseJson)
					token = reponseJson['result']['token']  # 获取token
					self.__requestHeaders['t'] = token  # 配置需要登录才能访问接口的headers
					await taskQueue.put(self.__requestHeaders)
	"""
	获取行业列表异步任务 相当于消费者 测试用
	"""
	async def get_industry_task(
			self,
			taskQueue: asyncio.queues, # 传入一个队列
	):
		headers = await taskQueue.get()
		#从队列获取headers
		self.set_request_headers(headers) #设置headers
		async with aiohttp.ClientSession() as session:
			async with session.get(
					self.config['env'][self.env]['requestDomain'] + self.config['get_industry_list']['requestPath'],
					headers=self.__requestHeaders, ) as response: #发送http异步请求
				reponseJson = await response.json()
				self.assertReponseResultCode(reponseJson) #判断json数据

	"""
	异步任务主函数，主要进行一些异步配置
	"""
	async def async_main(
			self,
	):
		taskQueue = asyncio.Queue() #定义一个队列，用于生产与消费
		getTokenTasks = list() #token任务列表
		get_industry_task = list() #获取行业信息任务列表
		userLoginUrl = self.config['env'][self.env]['requestDomain'] + self.config['users']['loginRequestPath'] #获取请求路径
		requestLimit = asyncio.Semaphore(self.__requestLimit) #配置并发数量
		taskNums = len(self.config['users']['student'])
		for i in self.config['users']['student']:
			getTokenTasks.append(self.async_get_token_task(userLoginUrl,{'phone':i['info']['phone'],'password':i['info']['password']}, requestLimit, taskQueue))
			get_industry_task.append(self.get_industry_task(taskQueue))
		await asyncio.gather(*getTokenTasks,*get_industry_task)
"""
主函数
"""
if __name__ == '__main__':
	asyncHttpTask = AsyncHttpTask() #创建异步http请求实例对象
	asyncHttpTask.set_request_env('dev') #配置环境
	asyncHttpTask.set_request_task_limit(2) #配置任务并发数量
	asyncio.run(asyncHttpTask.async_main()) #启动异步任务

