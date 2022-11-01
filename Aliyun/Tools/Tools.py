from datetime import datetime
import random
import urllib.parse

def getNowUTCTime():
	aliyunUTC = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ") #获取阿里云UTC时间格式
	aliyunUTCFormat = stringEncode(aliyunUTC)
	return aliyunUTCFormat
def stringEncode(str):
	return urllib.parse.quote(str)



def randomNumber():
	str = ""
	for i in range(14):
		ch = chr(random.randrange(ord('0'), ord('9') + 1))
		str += ch
	return str










