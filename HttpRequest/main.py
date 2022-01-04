from HttpRequest import HttpRequest
import requests
import test
if __name__ == '__main__':
	h = HttpRequest("https://www.baidu.com")
	h.set_verify(False)
	h.set_timeout(10)
	reponse = h.send_http_request(method='get')




