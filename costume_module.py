#模块
#一个py就是一个模块，可以提升代码的可维护性
#通过包（package）来管理目录
#每个package下面都有一个__init__.py,否则就把这个目录当成普通目录，其可以是个空文件，他本身就是个模块，并且模块名就是包名

# -*- coding:utf-8 -*-

'a test module'

__author__='Calmer'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print('helloworld')
	elif len(args)==2:
		print('Hello,%s' % args[1])
	else:
		print('too many arguments')

if __name__=='__main__':
	test()


#public var
abc='aaa'
judge=True
num=123

#special var
#__name__
#__author__
#__doc__等等

#private var or func
def _private_1(name):
	return 'hello,%s' % name

def _private_2(name):
	return 'Hi,%s' % name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)