#from 11 import my_abs 在当前目录名为11.py中导入my_abs函数

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

print(my_abs(-8))
