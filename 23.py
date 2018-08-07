#匿名函数
#只能有一个表达式，
print(list(map(lambda x:x*x,range(1,10))))


def build(x,y):
	return lambda : x*x+y*y


def is_odd(n):
	return n%2==1

L=list(filter(is_odd,range(1,20)))

print(L)


L=list(filter(lambda x:x%2==1,range(1,20)))

print(L)


#装饰器
def now():
	print('2018-8-7')

f=now
f()

print(now.__name__)
print(f.__name__)

#如果我们要增强now()的功能，比如在打印前后自动打印日志，但不希望修改now()的函数定义
#可以用修改器，decorator，其本质是高阶函数

def log(func):
	def wrapper(*args,**kw):
		print('call %s()' % func.__name__)
		return func(*args,**kw)
	return wrapper

#等价于执行了now=log(now)
@log
def now():
	print('2018-8-7')

now()


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s()' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

#等价于now=log('execute')(now)
@log('execute')
def now():
	print('2018-8-7')


now()
print(now.__name__)

#上述函数签名会有一定问题
#完整的decorator的写法
#不需要执行wrapper.__name__=func.__name__

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s()' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def add(x,y):
	return x+y

print(add(1,2))
print(add.__name__)


#带参的
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s()' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

#需要在定义wrapper前面加上@functools.wraps(func)

#practice
import time
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		t0=time.time()
		back=fn(*args,**kw)
		print('%s execute in %s ms' % (fn.__name__,time.time()-t0))
		return back
	return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('fail!')
elif s != 7986:
    print('fail!')


#new practice
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call')
		back=func(*args,**kw)
		print('end call')
		return back
	return wrapper

@log
def f():
	print('yes')

f()

print(f.__name__)

#practice3

def log(*text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			if len(text)!=0:
				print('%s %s()' % (*text,func.__name__))
			else:
				print('call %s()' % (func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log()
def f1():
	print('good')

@log('execute')
def f2():
	print('nice')

f1()
f2()