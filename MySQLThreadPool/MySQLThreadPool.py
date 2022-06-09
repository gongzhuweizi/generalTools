#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：MySQLThreadPool.py
@Author ：zhangyi
@Date ：2022/6/5 12:00 PM
'''

import importlib
from typing import Dict
from dbutils.pooled_db import PooledDB



class DataBase:
	def __init__(
			self,
			databaseType: str,
			databaseConfig: Dict
	):
		self.__databaseType = databaseType
		self.__databaseConfig = databaseConfig
		"""
		判断传入的数据库类型,选择不同的数据库驱动
		"""
		supportDatabaseType = {'mysql':'pymysql'} #配置数据库类型，可以添加
		if databaseType not in supportDatabaseType.keys():
			raise Exception('unsupported database type ' + self.__databaseType)
		else:
			self.__databaseCreator = importlib.import_module(supportDatabaseType[databaseType])
		"""
		创建连接池
		"""
		self.__pool = PooledDB(
			creator=self.__databaseCreator,
			mincached=0,
			maxcached=6,
			maxconnections=0,
			blocking=True,
			ping=0,
			**self.__databaseConfig
		)
		self.__sql : str = ''

	"""
	配置需要执行的数据库sql
	"""

	def set_mysql_sql(
			self,
			sql: str
	):
		"""
		:param sql: str
		"""
		self.__sql = sql

	def execute_only_sql(self,as_dict=True):
		dbConnection = None
		cursor = None
		try:
			dbConnection = self.__pool.connection()
			cursor = dbConnection.cursor()
			cursor.execute(self.__sql)
			sqlExecResult = cursor.fetchall()
			if sqlExecResult:
				if as_dict:
					fields = [tup[0] for tup in cursor._cursor.description]
					return [dict(zip(fields, row)) for row in sqlExecResult]
				return sqlExecResult
			return sqlExecResult
		except Exception as e:
			print('sql:[{}]meet error'.format(self.__sql))
			print(e.args[-1])
			return ()
		finally:
			if dbConnection:
				dbConnection.close()
			if cursor:
				cursor.close()

	def execute_manay(self, sql, data):
		dbConnection = None
		cursor = None
		try:
			dbConnection = self.__pool.connection()
			cursor = dbConnection.cursor()
			cursor.executemany(sql, data)
			dbConnection.commit()
			return True
		except Exception as e:
			print('[{}]meet error'.format(sql))
			print(e.args[-1])
			dbConnection.rollback()
			return False
		finally:
			if dbConnection:
				dbConnection.close()
			if cursor:
				cursor.close()


MySQL = DataBase(
	'mysql', {'user': 'profession', 'host': '10.1.1.119', 'password': '3ZFQCskBC3LtmZY8', 'database': 'es_base', 'port': 3306}
)


