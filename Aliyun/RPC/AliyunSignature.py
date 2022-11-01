# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/1 09:30
@Auth ： zy
@File ：AliyunSignature.py
@IDE ：PyCharm
@Motto: 孩童
"""
from RPCDataClass import RPCDataClass,PublicRequestParams
from ..Tools.Tools import getNowUTCTime, randomNumber, stringEncode
import base64
import hmac
from hashlib import sha1



class AliyunSignature():
	def __init__(
			self,
			RPCDataClass: RPCDataClass,
			AccessKeySecret: str

	):
		self.RPCDataClass = RPCDataClass
		self.AccessKeySecret = AccessKeySecret

	def __get_request_str(
			self,
	):
		request_str = RPCDataClass.aliyunEndpoint + '/?'
		+ "Timestamp=" + getNowUTCTime() \
		+ "&Format=" + RPCDataClass.publicRequestParams.format \
		+ "&AccessKeyId=" + RPCDataClass.publicRequestParams.accessKeyId \
		+ "&Action=" + RPCDataClass.publicRequestParams.action \
		+ "&SignatureMethod=" + RPCDataClass.publicRequestParams.signatureMethod \
		+ "&SignatureNonce=" + randomNumber \
		+ "&Version=" + RPCDataClass.publicRequestParams.version \
		+ "&SignatureVersion" + RPCDataClass.publicRequestParams.signatureVersion

	def getSignatureVersion(
			self,

	):
		publicRequestStr = "AccessKeyId=" + RPCDataClass.publicRequestParams.accessKeyId \
						   +"Action=" + RPCDataClass.publicRequestParams.action \
						   + "&Format=" + RPCDataClass.publicRequestParams.format \
						   + "&SignatureMethod=" + RPCDataClass.publicRequestParams.signatureMethod \
						   + "&SignatureNonce=" + randomNumber \
						   + "&SignatureVersion" + RPCDataClass.publicRequestParams.signatureVersion \
						   + "Timestamp=" + getNowUTCTime() \
						   + "&Version=" + RPCDataClass.publicRequestParams.version \


		stringToSign = RPCDataClass.httpMethod + "&" \
					   + stringEncode("/") + "&" +stringEncode(publicRequestStr)
		stringToSignBase64 =  base64.b64encode(hmac.new(self.AccessKeySecret+"&".encode(), stringToSign.encode(), sha1).digest()+"&")
		return stringToSignBase64
r = RPCDataClass('https://','ecs.aliyuncs.com',p,'GET')
p = PublicRequestParams('GetInstances','CreateInstance','JSON','......','','','HMAC-SHA1','1.0',a.getSignatureVersion())
a = AliyunSignature(r,)


