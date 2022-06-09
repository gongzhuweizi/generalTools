# -*-coding:utf-8 -*-
"""
@Author: zhangyi
@Time: 2021/12/31 10:08 上午
@File: OperationMySQL.py
@IDE: PyCharm
"""
from typing import Tuple, Any

import pymysql
from MySQLExceptions import MySQLCustomExcetion
"""
mysql操作工具类，传入host，user，password，db参数
"""


class OperationMySQL:



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
		conn = None
		cur = None
		try:
			conn = self.pool.connection()
			cur = conn.cursor()
			cur.execute(sql)
			rst = cur.fetchall()
			if rst:
				if as_dict:
					fields = [tup[0] for tup in cur._cursor.description]
					return [dict(zip(fields, row)) for row in rst]
				return rst
			return rst

		except Exception as e:
			print('sql:[{}]meet error'.format(sql))
			print(e.args[-1])
			return ()
		finally:
			if conn:
				conn.close()
			if cur:
				cur.close()










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


