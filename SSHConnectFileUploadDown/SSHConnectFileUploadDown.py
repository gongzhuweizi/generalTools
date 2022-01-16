#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：generalTools
@File ：SSHConnectFileUploadDown.py
@Author ：zhangyi
@Date ：2022/1/5 11:21 AM
使用paramiko模块实现远程执行命令、上传、下载文件
'''
import paramiko
import time
from SSHDataClass import ExecCommandDataClass

"""
paramiko远程操作主机
"""


class SSHConnectFileUploadDown():
	def __init__(
			self,
			hostname: str = None,
			port: int = 22,
			username: str = None,
	) -> object:
		"""
		@param hostname: 连接主机地址
		@param port: ssh端口
		@param username: 连接用户名
		@param password: 连接密码
		@param private_key_file: 使用私钥进行连接
		@rtype: object
		"""
		self._hostname: str = hostname
		self._port: int = port
		self._username: str = username
		self._password: str = None
		self._private_key_file: str = None
		self._command: str = None
		self._src_file_dir: str = None
		self._des_file_dir: str = None
		self._ssh: paramiko.SSHClient = None
		self._transport = None
		self._sftp = None

	"""
	配置主机地址
	"""

	def set_ssh_hostname(
			self,
			hostname: str
	) -> object:
		"""
		@param hostname: 配置主机地址
		@rtype: object
		"""
		self._hostname = hostname

	"""
	获取主机地址
	"""

	def get_ssh_hostname(
			self
	) -> str:
		"""
		@return: 返回一个主机地址
		"""
		return self._hostname

	"""
	配置ssh端口
	"""

	def set_ssh_port(
			self,
			port: int
	) -> object:
		"""
		@param port: 配置端口
		@rtype: object
		"""
		self._port = port

	"""
	获取ssh端口
	"""

	def get_ssh_port(
			self
	) -> int:
		"""
		@return: 返回ssh端口
		"""
		return self._port

	"""
	配置ssh用户名
	"""

	def set_ssh_username(
			self,
			username: str
	) -> object:
		"""
		@param username: 配置ssh用户名称
		@rtype: object
		"""
		self._username = username

	"""
	获取ssh用户名
	"""

	def get_ssh_username(
			self
	) -> str:
		"""
		@rtype: str
		@return: 返回ssh用户名
		"""
		return self._username

	"""
	配置ssh密码
	"""

	def set_ssh_password(
			self,
			password: str
	) -> object:
		"""
		@param password: 配置ssh密码
		@rtype: object
		"""
		self._password = password

	"""
	获取ssh密码
	"""

	def get_ssh_password(
			self
	) -> str:
		"""
		@return: 返回ssh密码
		@rtype: str
		"""
		return self._password

	"""
	配置ssh私钥
	"""

	def set_private_key_file(
			self,
			private_key_file: str
	) -> object:
		"""
		@rtype: object
		@param private_key_file: 私钥文件路径
		"""
		self._private_key_file = private_key_file

	def get_private_key_file(
			self
	) -> str:
		"""
		@return: 返回ssh密钥路径
		@rtype: str
		"""
		return self._private_key_file

	"""
	配置远程执行的命令
	"""

	def set_exec_command(
			self,
			command: str
	) -> object:
		"""
		@rtype: object
		@param command: 需要远程执行的命令
		"""
		self._command = command

	def get_exec_command(
			self
	) -> str:
		"""
		@rtype: str
		@return: 返回需要执行的命令
		"""
		return self._command

	"""
	设置文件原路径，用于文件的远程上传、下载
	"""

	def set_src_file_dir(
			self,
			src_file_dir: str
	) -> object:
		"""
		@param src_file_dir: 文件源路径
		@rtype: object
		"""
		self._src_file_dir = src_file_dir

	"""
	获取源文件路径
	"""

	def get_src_file_dir(
			self
	) -> str:
		"""
		@rtype: str
		@return: 返回源文件路径
		"""
		return self._src_file_dir

	"""
	设置目录文件路径
	"""

	def set_des_file_dir(
			self,
			des_file_dir: str

	) -> object:
		"""
		@param des_file_dir: 目的文件路径
		@rtype: str
		"""
		self._des_file_dir = des_file_dir

	"""
	获取目的文件路径
	"""

	def get_des_file_dir(
			self
	) -> str:
		"""
		@return: 返回目的文件路径
		@rtype: str
		"""
		return self._des_file_dir

	"""
	获取远程ssh连接，使用transport，用户名密码的方式
	"""

	def __get_ssh_transport_password(
			self
	) -> object:
		"""
		@rtype: ssh 对象
		@return: ssh object
		"""
		try:
			self._transport = paramiko.Transport((self._hostname, self._port))
			self._transport.connect(
				username=self._username,
				password=self._password
			)
			self._ssh = paramiko.SSHClient()
			self._ssh._transport = self._transport
			self._sftp = paramiko.SFTPClient.from_transport(self._transport)
		except Exception as e:
			self._transport.close()
			print("使用账号密码连接失败-" + str(e))
			exit(127)

	"""
	获取远程执行命令结果，返回一个数据类字典类型，stdin，stdout
	"""

	def __get_ssh_transport_private_key(
			self
	) -> object:
		try:
			self._transport = paramiko.Transport((self._hostname, self._port))
			keyfile = paramiko.RSAKey.from_private_key_file(self._private_key_file)
			self._transport.connect(
				username=self._username,
				pkey=keyfile
			)
			self._ssh = paramiko.SSHClient()
			self._ssh._transport = self._transport
			self._sftp = paramiko.SFTPClient.from_transport(self._transport)
		except Exception as e:
			self._transport.close()
			print("使用密钥连接失败-" + str(e))
			exit(127)

	"""
	私有函数，远程执行命令，接收一个ssh参数
	"""

	def __exec_remote_command(
			self,
	) -> ExecCommandDataClass:
		"""

		@rtype: ExecCommandDataClass对象
		@return: ExecCommandDataClass对象
		"""
		try:
			stdin, stdout, stderr = self._ssh.exec_command(self._command)
			time.sleep(0.5)
			if stdout is not None:
				result = ExecCommandDataClass(
					stdin=stdin,
					stdout=stdout.readlines(),
					stderr=stderr
				)
			else:
				result = ExecCommandDataClass(
					stdin=stdin,
					stdout=stdout,
					stderr=stderr.readlines()
				)

			return result
		except Exception as e:
			print("执行命令失败！" + str(e))
			exit(127)
		finally:
			self._transport.close()

	"""
	获取远程执行命令结果，返回dataclass数据类对象
	"""

	def get_exec_remote_command_result(
			self
	) -> ExecCommandDataClass:
		"""
		@rtype: ExecCommandDataClass
		"""
		if self._password != None and self._private_key_file == None:
			self.__get_ssh_transport_password()
			result = self.__exec_remote_command()
			return result
		elif self._private_key_file != None and self._password == None:
			self.__get_ssh_transport_private_key()
			result = self.__exec_remote_command()
			return result
		elif self._password != None and self._private_key_file != None:
			try:
				self.__get_ssh_transport_password()
			except Exception as e:
				print("使用密码连接失败" + e)
				try:
					self.__get_ssh_transport_private_key()
				except Exception as e:
					print("账号密码均连接失败！")
			return self.__exec_remote_command(self._ssh)
		elif self._password == None and self._private_key_file == None:
			print("密码或者密码全部为空，请配置服务器的密码或者密钥进行远程连接！")
		else:
			print("连接失败，未知错误！")

	"""
	远程执行文件上传
	"""

	def __put_file(
			self
	) -> object:
		"""
		@return: 返回一个文件上传返回对象
		"""
		result = self._sftp.put(
			localpath=self._src_file_dir,
			remotepath=self._des_file_dir
		)
		self._transport.close()
		if result is not None:
			return result

	"""
	远程执行文件下载
	"""

	def __download_file(
			self
	) -> object:
		"""
		@return: 返回一个下载文件返回结果对象
		"""
		result = self._sftp.get(
			remotepath=self._src_file_dir,
			localpath=self._des_file_dir
		)
		self._transport.close()
		if result is not None:
			return result

	def put_file_result(
			self
	):
		if self._password != None and self._private_key_file == None:
			self.__get_ssh_transport_password()
			result = self.__put_file()
			return result
		elif self._private_key_file != None and self._password == None:
			self.__get_ssh_transport_private_key()
			result = self.__put_file()
			return result
		elif self._password != None and self._private_key_file != None:
			try:
				self.__get_ssh_transport_password()
			except Exception as e:
				print("使用密码连接失败" + e)
				try:
					self.__get_ssh_transport_private_key()
				except Exception as e:
					print("账号密码均连接失败！")
			return self.__put_file()
		elif self._password == None and self._private_key_file == None:
			print("密码或者密码全部为空，请配置服务器的密码或者密钥进行远程连接！")
		else:
			print("连接失败，未知错误！")


	"""
	获取下载文件返回结果
	"""
	def get_file_result(
			self
	) -> object :
		"""
		@rtype: object
		@return: 返回一个paramiko执行对象
		"""
		if self._password != None and self._private_key_file == None:
			self.__get_ssh_transport_password()
			result = self.__download_file()
			return result
		elif self._private_key_file != None and self._password == None:
			self.__get_ssh_transport_private_key()
			result = self.__download_file()
			return result
		elif self._password != None and self._private_key_file != None:
			try:
				self.__get_ssh_transport_password()
			except Exception as e:
				print("使用密码连接失败" + e)
				try:
					self.__get_ssh_transport_private_key()
				except Exception as e:
					print("账号密码均连接失败！")
			return self.__download_file()
		elif self._password == None and self._private_key_file == None:
			print("密码或者密码全部为空，请配置服务器的密码或者密钥进行远程连接！")
		else:
			print("连接失败，未知错误！")
