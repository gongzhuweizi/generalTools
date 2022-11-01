from dataclasses import dataclass
from typing import Any


@dataclass
class PublicRequestParams:
	action: str  # API的名称。您可以访问阿里云OpenAPI开发者门户，搜索您想调用的 OpenAPI
	version: str  # API 版本。您可以访问阿里云OpenAPI开发者门户，查看您调用 OpenAPI 对应的 API 版本
	format: str  # 指定接口返回数据的格式。可以选择 JSON 或者 XML。默认为 XML。
	accessKeyId: str  # 阿里云访问密钥ID。您可以在RAM 控制台 查看您的 AccessKeyId。如需创建 AccessKey，请参见创建 AccessKey
	signatureNonce: str  # 签名唯一随机数。用于防止网络重放攻击，建议您每一次请求都使用不同的随机数。
	timestamp: str  # 请求的时间戳。按照ISO8601标准表示，并需要使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ。
	signatureMethod: str  # 签名方式。目前为固定值 HMAC-SHA1
	signatureVersion: str  # 签名算法版本。目前为固定值 1.0
	signature: str  # 请求签名，用户请求的身份验证。详细签名机制，请参见签名机制。


@dataclass
class RPCDataClass:
	httpProtocol: str  # 您可以查阅不同云产品的 API 参考文档进行配置。支持通过HTTP或HTTPS协议进行请求通信。为了获得更高的安全性，推荐您使用HTTPS协议发送请求。取值范围为https://或者
	# http://
	aliyunEndpoint: str  # 您可以查阅不同云产品的 API 参考文档进行配置。支持通过HTTP或HTTPS协议进行请求通信。为了获得更高的安全性，推荐您使用HTTPS协议发送请求。取值范围为https://或者
	# http://
	publicRequestParams: PublicRequestParams  # 您可以查阅不同云产品的 API 参考文档进行配置。支持通过HTTP或HTTPS协议进行请求通信。为了获得更高的安全性，推荐您使用HTTPS
	# 协议发送请求。取值范围为https://或者 http://
	customParams: Any  # 您可以查阅不同云产品的 API 参考文档进行配置。支持通过HTTP或HTTPS协议进行请求通信。为了获得更高的安全性，推荐您使用HTTPS协议发送请求。取值范围为https://或者
	# http://
	httpMethod: str  # RPC 请求Method支持 POST 或者 GET
