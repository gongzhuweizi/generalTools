import requests
from requests import  Response
from requests.auth import HTTPBasicAuth
from typing import Union
from typing import Any,Optional,Dict

"""
http请求工具类
"""


class HttpRequest():
	"""
	初始化 传入主机地址
	"""


	def __init__(
			self,
			url: Union[str, bytes]
	):
		"""
		@param host: str
		"""
		self.__url = url

	"""
	私有属性
	"""
	__headers: Optional[Dict] = None
	__params:  Optional[Dict]= None
	__data: Optional[Dict] = None
	__cookies: Optional[Dict] = None
	__files: Union[Any, None] = None
	__auth: Union[Any, None] = None
	__timeout: Union[Any, None] = None
	__allow_redirects: bool = True
	__proxies: Union[Any, None] = None
	__hooks: Union[Any, None] = None
	__stream: Union[Any, None] = None
	__verify: bool = True
	__cert: Union[Any, None] = None
	__json: Union[Any, None]  = None
	"""

	"""

	def __get_params_dict(self):
		return {'timeout':self.__timeout}
	"""
	可以配置主机地址
	"""

	def set_url(
			self,
			url: Union[str, bytes]
	):
		"""
		@param host:  str | bytes
		"""
		self.__url = url

	"""
	配置post data数据
	"""

	def set_data(
			self,
			data: Optional[Dict]
	):
		"""
		@param data: dict
		"""
		self.__data = data

	"""
	获取post 数据
	"""

	def get_data(
			self
	):
		"""
		@rtype: object
		"""
		return self.__data

	"""
	配置headers
	"""

	def set_header(
			self,
			headers: Optional[Dict]
	):
		"""
		@param headers: dict
		"""
		self.__headers = headers

	"""
	配置请求参数
	"""

	def set_params(
			self,
			params: Optional[Dict]
	):
		"""
		@param params: dict
		"""
		self.__params = params

	"""
	配置cookies
	"""

	def set_cookies(
			self,
			cookies: Optional[Dict]
	):
		"""
		@param cookies: dict
		"""
		self.__cookies = cookies

	"""
	配置files
	"""

	def set_files(
			self,
			files: Union[None, Any]
	):
		"""
		@param files: None,Any
		"""
		self.__files = files

	"""
	配置http认证
	"""

	def set_auth(
			self,
			auth: object
	):
		"""
		@param auth: object
		"""
		self.__auth = auth

	"""
	配置超时时间
	"""

	def set_timeout(
			self,
			timeout: Union[None, Any]
	):
		"""
		@param timeout: None | Any
		"""
		self.__timeout = timeout

	"""
	配置是否允许重定向
	"""

	def set_allow_redirects(
			self,
			allow_redirects: bool
	):
		self.__allow_redirects = allow_redirects

	"""
	配置代理
	"""

	def set_proxies(
			self,
			proxies: Union[Any, None]
	):
		"""
		@param proxies: None | Any
		"""
		self.__proxies = proxies

	"""
	配置钩子行数
	"""

	def set_hooks(
			self,
			hooks: Union[Any, None]
	):
		"""
		@param hooks: Any | None
		"""
		self.__hooks = hooks

	"""
	配置stream
	"""

	def set_stream(
			self,
			stream: Union[Any, None]
	):
		"""
		@param stream: Any | None
		"""
		self.__stream = stream

	"""
	获取stream
	"""

	def get_stream(
			self
	) -> Any:
		"""
		@rtype: Any
		"""
		return self.__stream

	"""
	配置警告⚠️
	"""

	def set_verify(
			self,
			verify: bool
	):
		"""
		@param verify: bool
		"""
		self.__verify = verify

	"""
	获取警告
	"""

	def get_verify(
			self
	) -> bool:
		"""
		@rtype: bool
		"""
		return self.__verify

	"""
	配置证书
	"""

	def set_cert(
			self,
			cert: Union[Any, None]
	):
		"""
		@param cert: Any | None
		"""
		self.__cert = cert

	"""
	获取证书
	"""

	def get_cert(
			self
	) -> Any:
		"""
		@rtype: Any
		"""
		return self.__cert

	"""
	配置json header头
	"""

	def set_json(
			self,
			json: Union[Any, None]
	):
		"""
		@param json: object
		"""
		self.__json = json

	"""
	获取header头格式
	"""

	def get_json(
			self
	) -> Union[Any, None]:
		"""
		@rtype: Any | None
		"""
		return self.__json

	"""
	获取钩子函数
	"""

	def get_hooks(
			self
	) -> Union[Any, None]:
		"""
		@rtype: Any | None
		"""
		return self.__hooks

	"""
	获取代理
	"""

	def get_proxies(
			self
	) -> Union[None, Any]:
		"""
		@rtype: None | Any
		"""
		return self.__proxies

	"""
	获取是否允许重定向
	"""

	def get_allow_redirects(
			self
	) -> bool:
		"""

		@rtype: bool
		"""
		return self.__allow_redirects

	"""
	获取超时时间
	"""

	def get_timeout(
			self
	) -> Union[None, Any]:
		"""
		@rtype: object
		"""
		return self.__timeout

	"""
	获取请求地址
	"""

	def get_url(
			self
	) -> Union[str, bytes]:
		"""
		@rtype: str | bytes
		"""
		return self.__url

	"""
 	获取请求headers
	"""

	def get_headers(
			self
	) -> Optional[Dict]:
		"""
		@rtype: dict
		"""
		return self.__headers

	"""
	获取请求参数
	"""

	def get_params(
			self
	) -> Optional[Dict]:
		"""
		@return: dict
		"""
		return self.__params

	"""
	获取cookies
	"""

	def get_cookies(
			self
	) -> Optional[Dict]:
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
			method: str = None
	) -> Union [Response,Dict]:

		self.__method = method
		if self.__method == 'get':
			response = requests.get(
				self.__url,
				params = None,
				**self.__get_params_dict()
			)
			return response
		elif self.__method == 'post':
			response = requests.post(self.__url,
									 data = self.__data,
									 json = self.__json,
									 **self.__get_params_dict()
									 )
			return response
		elif self.__method == 'delete':
			response = requests.delete(self.__url,
									   **self.__get_params_dict()
									   )
			return response
		elif self.__method == 'put':
			response = requests.put(self.__url,
									data=self.__data,
									**self.__get_params_dict()
									)
			return response
		else:
			return {'code': 400, 'message': '请求方式错误'}
	@classmethod
	def analysis_reponse_json_data(
			cls,
			data : Response

	) -> object :
		data_json = data.json()
		return data_json
	@classmethod
	def analysis_reponse_text_data(
			cls,
			data : Response
	) -> object :
		data_text = data.text
		return data_text


