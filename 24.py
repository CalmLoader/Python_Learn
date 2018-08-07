#偏函数

#后面的是当前的进制是什么即字符串中数是什么进制

#从而全部转换成10进制
print(int('12345'))
print(int('17',base=8))   #15
print(int('0xff',base=16))    #255
print(int('12345',8))

print(int('111111111',base=2))    #255
#偏函数
def int2(x,base=2):
	return int(x,base)

print(int2('10011001'))
print(int2('10001000'))

#自带的偏函数
import functools
int2_=functools.partial(int,base=2)
print(int2_('10011001'))
#也可调用,将参数设置为10
print(int2_('10011001',base=10))

#另外的偏函数
max2=functools.partial(max,10)
print(max2(5,6,7))