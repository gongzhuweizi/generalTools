'''
@Project ：generalTools
@File ：DataClassRequestParams.py
@Author ：zhangyi
@Date ：2022/1/4 16:17 PM
'''
from HttpRequest import HttpRequest
if __name__ == '__main__':
	h = HttpRequest("https://www.baidu.com")
	h.set_verify(False)
	h.set_timeout(10)
	reponse = h.send_http_request(method='get')
	print(h.analysis_reponse_text_data(reponse))
	print(h.get_reponse_status_code(reponse))





