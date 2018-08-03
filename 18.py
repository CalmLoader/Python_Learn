#生成器
import math
L=[x*x for x in range(10)]  #列表生成式
print(L)
g=(x*x for x in range(10))	#生成器
print(g,next(g),next(g),next(g),next(g))

g=(x*x for x in range(10))
#常用for进行输出生成器中内容
for n in g:
	print(n)

#普通函数
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'

fib(6)

#生成器
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'

f=fib(6)
for n in f:
	print(n)

#例子
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3

o=odd()
print(next(o))
print(next(o))
print(next(o))


#继续fib,要想捕获函数return
g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except Exception as e:
		print('Generator value:',e.value)
		break

#practice  第n行的m个数可以表示为C(n-1,m-1)

def calC(n,m):
	r1,r2,r3=1,1,1
	if n==0:
		r1=1
	else:
		mul=1
		for i in range(1,n+1):
			mul=mul*i
		r1=mul

	if m==0:
		r2=1
	else:
		mul=1
		for i in range(1,m+1):
			mul=mul*i
		r2=mul

	if (m-n)==0:
		r3=1
	else:
		mul=1
		for i in range(1,n-m+1):
			mul=mul*i
		r3=mul
	return r1/(r2*r3)

def triangles():
	i=1
	while True:
		L=[]
		for n in range(1,i+1):
			L.append(calC(i-1,n-1))
		i=i+1
		yield L
	return 'done'
	
#测试
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('success!')
else:
    print('fail!')
