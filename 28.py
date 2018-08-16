import requests,time

if __name__ == '__main__':
	target='https://blog.csdn.net/qq_34406755/article/details/81227746'
	for i in range(2):
		req=requests.get(url=target)
		print(i)
		time.sleep(10)
