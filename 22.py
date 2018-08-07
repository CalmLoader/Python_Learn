#返回函数

#普通函数
def calc_sum(*args):
	ax=0
	for n in args:
		ax=ax+n
	return ax

#返回函数
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

#调用
f=lazy_sum(1,3,5,7,9)
print(f())

#闭包
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3=count()
#结果都为9
print(f1(),f2(),f3())

#要让循环引用

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for n in range(1,4):
		fs.append(f(n))
	return fs

f1,f2,f3=count()
#结果为1,4,9
print(f1(),f2(),f3())

#lambda
def count():
	def f(j):
		return lambda :j*j
	fs=[]
	for n in range(1,4):
		fs.append(f(n))
	return fs

f1,f2,f3=count()
#结果为1,4,9
print(f1(),f2(),f3())

#practice
def createCounter():
	n=0
	def counter():
		nonlocal n
		n=n+1
		return n
	return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('success!')
else:
    print('fail!')