from HttpRequest import HttpRequest
if __name__ == '__main__':
	h = HttpRequest("https://www.baidu.com")
	cmd = h.send_http_request('get')
	print(cmd.text)

