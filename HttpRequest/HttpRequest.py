import requests
from requests.auth import HTTPBasicAuth
from typing import Union
from typing import Any

"""
http请求工具类
"""
class HttpRequest():
	"""
	初始化 传入主机地址
	"""
	def __init__(
			self,
			url : Union[str,bytes]
	):
		"""
		@param host: str
		"""
		self.__url = url
	"""
	私有属性
	"""
	__headers : dict = None
	__params : dict = None
	__data : dict = None
	__cookies : dict = None
	__files : Union[Any,None] = None
	__auth : Union[Any,None]  = None
	__timeout : Union[Any,None] = None
	__allow_redirects : bool = True
	__proxies : Union[Any,None] = None
	__hooks : Union[Any,None] = None
	__stream : Union[Any,None] = None
	__verify: bool  = True
	__cert : Union[Any,None] = None
	__json : Union[Any,None] = None
	"""
	可以配置主机地址
	"""
	def set_url(
			self,
			url : Union[str,bytes]
	) -> object :
		"""
		@param host:  str | bytes
		"""
		self.__url = url
	"""
	配置post data数据
	"""
	def set_data(
			self,
			data : dict
	) -> object:
		"""
		@param data: dict
		"""
		self.__data  = data
	"""
	获取post 数据
	"""
	def get_data(
			self
	) -> object:
		"""
		@rtype: object
		"""
		return  self.__data
	"""
	配置headers
	"""
	def set_header(
			self,
			headers : dict
	) -> object :
		"""
		@param headers: dict
		"""
		self.__headers = headers
	"""
	配置请求参数
	"""
	def set_params(
			self,
			params : dict
	) ->object :
		"""
		@param params: dict
		"""
		self.__params = params
	"""
	配置cookies
	"""
	def set_cookies(
			self,
			cookies : dict
	) -> object :
		self.__cookies = cookies
	"""
	配置files
	"""
	def set_files(
			self,
			files : Union[None,Any]
	) -> object:
		self.__files = files
	"""
	配置http认证
	"""
	def set_auth(
			self,
			auth : object
	) -> object :
		"""
		@param auth: object
		"""
		self.__auth = auth
	"""
	配置超时时间
	"""
	def set_timeout(
			self,
			timeout : Union[None,Any]
	) -> object:
		"""
		@param timeout: None | Any
		"""
		self.__timeout = timeout
	"""
	配置是否允许重定向
	"""
	def set_allow_redirects(
			self,
			allow_redirects : bool
	) -> object:
		self.__allow_redirects = allow_redirects
	"""
	配置代理
	"""
	def set_proxies(
			self,
			proxies : Union[Any,None]
	) -> object:
		"""
		@param proxies: None | Any
		"""
		self.__proxies = proxies
	"""
	配置钩子行数
	"""
	def set_hooks(
			self,
			hooks : Union[Any,None]
	) -> object:
		"""
		@param hooks: Any | None
		"""
		self.__hooks = hooks
	"""
	配置stream
	"""
	def set_stream(
			self,
			stream : Union[Any,None]
	) -> object:
		"""
		@param stream: Any | None
		"""
		self.__stream = stream
	"""
	获取stream
	"""
	def get_stream(
			self
	) -> object :
		"""
		@rtype: object
		"""
		return self.__stream

	"""
	配置警告⚠️
	"""
	def set_verify(
			self,
			verify : Union[Any,None]
	) -> object:
		"""
		@param verify: bool
		"""
		self.__verify = verify
	"""
	获取警告
	"""
	def get_verify(
			self
	) -> bool :
		"""
		@rtype: bool
		"""
		return  self.__verify
	"""
	配置证书
	"""
	def set_cert(
			self,
			cert : Union[Any,None]
	) -> object:
		"""
		@param cert: Any | None
		"""
		self.__cert = cert
	"""
	获取证书
	"""
	def get_cert(
			self
	) -> object:
		"""
		@rtype: object
		"""
		return  self.__cert
	"""
	配置json header头
	"""
	def set_json(
			self,
			json : Union[Any,None]
	) -> object :
		"""
		@param json: object
		"""
		self.__json = json
	"""
	获取header头格式
	"""
	def get_json(
			self
	) -> object:
		"""
		@rtype: object
		"""
		return  self.__json
	"""
	获取钩子函数
	"""
	def get_hooks(
			self
	) -> Union[Any,None]:
		"""
		@rtype: Any | None
		"""
		return self.__hooks

	"""
	获取代理
	"""
	def get_proxies(
			self
	) -> Union[None,Any]:
		"""
		@rtype: None | Any
		"""
		return self.__proxies
	"""
	获取是否允许重定向
	"""
	def get_allow_redirects(
			self
	) -> bool :
		return self.__allow_redirects
	"""
	获取超时时间
	"""
	def get_timeout(
			self
	) -> Union[None,Any]:
		"""
		@rtype: object
		"""
		return self.__timeout
	"""
	获取请求地址
	"""
	def get_host(
			self
	) -> str :
		"""

		@rtype: str
		"""
		return self.__host
	"""
 	获取请求headers
	"""
	def get_headers(
			self
	) -> dict :
		"""
		@rtype: dict
		"""
		return self.__headers
	"""
	获取请求参数
	"""
	def get_params(
			self
	) -> dict :
		"""
		@return: dict
		"""
		return self.__params
	"""
	获取cookies
	"""
	def get_cookies(
			self
	) -> dict :
		"""
		@return: dict
		"""
		return self.__cookies
	"""
	获取files
	"""
	def get_files(
			self
	) -> object:
		"""
		@return: object
		"""
		return self.__files
	def send_http_request(
			self,
			method : str
	) -> object:
		self.__method = method
		if self.__method == 'get':
			response = requests.get(
			url = self.__url,
			params = self.__params,
			data = self.__data,
			headers = self.__headers,
			cookies = self.__cookies,
			files = self.__files,
			auth = self.__auth,
			timeout = self.__timeout,
			allow_redirects = self.__allow_redirects,
			proxies = self.__proxies,
			hooks = self.__hooks,
			stream = self.__stream,
			verify = self.__verify,
			cert = self.__cert,
			json = self.__json )
			return response
		elif self.__method == 'post':
			response = requests.post(
			url=self.__url,
			params=self.__params,
			data=self.__data,
			headers=self.__headers,
			cookies=self.__cookies,
			files=self.__files,
			auth=self.__auth,
			timeout=self.__timeout,
			allow_redirects=self.__allow_redirects,
			proxies=self.__proxies,
			hooks=self.__hooks,
			stream=self.__stream,
			verify=self.__verify,
			cert=self.__cert,
			json=self.__json)
			return response
		elif self.__method == 'delete':
			response = requests.post(
			url=self.__url,
			params=self.__params,
			data=self.__data,
			headers=self.__headers,
			cookies=self.__cookies,
			files=self.__files,
			auth=self.__auth,
			timeout=self.__timeout,
			allow_redirects=self.__allow_redirects,
			proxies=self.__proxies,
			hooks=self.__hooks,
			stream=self.__stream,
			verify=self.__verify,
			cert=self.__cert,
			json=self.__json)
			return response
		elif self.__method == 'put':
			response = requests.post(
			url=self.__url,
			params=self.__params,
			data=self.__data,
			headers=self.__headers,
			cookies=self.__cookies,
			files=self.__files,
			auth=self.__auth,
			timeout=self.__timeout,
			allow_redirects=self.__allow_redirects,
			proxies=self.__proxies,
			hooks=self.__hooks,
			stream=self.__stream,
			verify=self.__verify,
			cert=self.__cert,
			json=self.__json)
			return response
		else:
			return {'code':400,'message':'请求方式错误'}

























