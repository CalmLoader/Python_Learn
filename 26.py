#爬虫

from bs4 import BeautifulSoup

import requests




def _getOneChapter(target):
	#target='http://www.biqukan.com/1_1094/5403177.html'
	req=requests.get(url=target)
#	print(req.text)
	html=req.text
	bf=BeautifulSoup(html)
	texts=bf.find_all('div',class_='showtxt')
	print(texts[0].text.replace('\xa0'*8,'\n'))


def test():
	server='http://www.biqukan.com'
	target='http://www.biqukan.com/1_1094/'
	req=requests.get(url=target)
	html=req.text
	bf=BeautifulSoup(html)
	texts=bf.find_all('div',class_='listmain')
	a_bf=BeautifulSoup(str(texts[0]))
	a=a_bf.find_all('a')
	a=a[15:]
	#print(a[2])
	#print(a)
	for each in a[0:10]:
		print(each.string,server+each.get('href'))
		print(each.string+'\n')
		_getOneChapter(server+each.get('href'))
	#print(a)



if __name__=='__main__':
	test()