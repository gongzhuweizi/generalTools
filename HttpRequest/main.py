'''
@Project ：generalTools
@File ：DataClassRequestParams.py
@Author ：zhangyi
@Date ：2022/1/4 16:17 PM
'''
import time

from HttpRequest import HttpRequest

if __name__ == '__main__':
	while True:
		h = HttpRequest("https://beta-careeradmin.wanxue.cn")
		h.set_verify(False)
		h.set_timeout(1)
		reponse = h.send_http_request(method='get')
		if h.get_reponse_status_code(reponse) == 200:
			print("访问成功！")
		else:
			print("访问失败！")
		time.sleep(5)

