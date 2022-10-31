# -*-coding:utf-8 -*-
"""
@Author: zhangyi
@Time: 2021/12/31 10:08 上午
@File: OperationMySQL.py
@IDE: PyCharm
"""
from typing import Tuple, Any

import pymysql
from OperationMySQL.MySQLExceptions import MySQLCustomExcetion
"""
mysql操作工具类，传入host，user，password，db参数
"""


class OperationMySQL:
	def __init__(
			self,
			host=None,
			user=None,
			password=None,
	) -> None:
		"""
		:param host: str
		:param user: str
		:param password:  str
		:param db: str
		"""
		self._sql: str = ''
		self._host: str = host
		self._user: str = user
		self._password: str = password
		self._db: str
		self._port: int = 3306  # port属性默认为3306，可以通过set自定义
		self._charset: str = 'utf8'  # charset默认属性为utf-8，可以通过set自定义
	"""
	配置数据连接地址
	"""
	def set_mysql_host(
			self,
			host: str
	):
		"""
		:param host: str
		"""
		self._host = host
	"""
	配置数据库用户名
	"""
	def set_mysql_user(
			self,
			user: str
	):
		"""
		:param user: str
		"""
		self._user = user
	"""
	配置数据库密码
	"""
	def set_mysql_password(
			self,
			password: str
	):
		"""
		:param password: str
		"""
		self._password = password
	"""
	配置需要连接的数据库
	"""
	def set_mysql_db(
			self,
			db: str
	):
		"""
		:param db: str
		"""
		self._db = db
	"""
	配置数据库端口
	"""
	def set_mysql_port(
			self,
			port: int
	):
		"""
		:param port: int
		"""
		self._port = port
	"""
	配置数据库连接字符集
	"""
	def set_mysql_charset(
			self,
			charset: str
	):
		"""
		:param charset: str
		"""
		self._charset = charset
	"""
	获取连接数据库地址
	"""
	def get_mysql_host(
			self
	) -> str:
		"""
		:rtype:
		"""
		return self._host
	"""
	获取数据库连接用户
	"""
	def get_mysql_user(
			self
	) -> str:
		"""
		:rtype: str
		"""
		return self._user
	"""
	获取数据连接密码
	"""
	def get_mysql_password(
			self
	) -> str:
		"""
		:rtype: str
		"""
		return self._password
	"""
	获取连接数据库名称
	"""
	def get_mysql_db(
			self
	) -> str:
		"""
		:rtype: str
		"""
		return self._db
	"""
	获取连接数据库端口
	"""
	def get_mysql_port(
			self
	) -> int:
		"""

		:rtype: int
		"""
		return self._port
	"""
	获取数据库连接字符集
	"""
	def get_mysql_charset(
			self
	) -> str:
		"""
		:rtype: str
		"""
		return self._charset
	"""
	获取数据连接对象
	"""

	def get_mysql_connect(
			self
	) -> pymysql.Connect:
		"""
		:rtype: pymysql.Connect
		"""
		conn = pymysql.Connect(
			host=self._host,
			port=self._port,
			user=self._user,
			password=self._password,
			db=self._db,
			charset=self._charset
		)
		return conn
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
		self._sql = sql
	"""
	获取需要执行的数据库sql
	"""
	def get_mysql_sql(
			self
	) -> str:
		"""
		:rtype: str
		"""
		return self._sql
	"""
	检查数据库sql是否为空
	"""

	def __check_sql_isNull(
			self
	):
		if self.get_mysql_sql() == '':
			raise MySQLCustomExcetion.MySQlSqlNullExcetion("sql为空！")
	"""
	单条sql的执行
	"""
	def execute_only_sql(
			self,
			execute_type : str,
			connect
	) -> Tuple[Tuple[Any, ...], ...]:
		"""
		:rtype: str or int
		"""
		self.__check_sql_isNull()
		cursor = connect.cursor()
		try:

			result = cursor.execute(self._sql)
			if execute_type == 'select':
				return cursor.fetchall()
			elif execute_type == 'update' or execute_type=="insert" or execute_type == 'delete':
				if result:
					print("执行成功")
					connect.commit()
				else:
					print("执行失败")
			else:
				print("参数错误")
		except Exception as e:
			print("执行sql失败"+str(e))
			cursor.close()


