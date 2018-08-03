#高阶函数
#变量名是函数
print(abs(-10))
print(abs)

f=abs
print(f(-1))

#函数名也是变量

#传入函数，最简单的高阶函数
def add(x,y,f):
	return f(x)+f(y)

#其中abs是求绝对值的函数名
print(add(-5,6,abs))

#map
L=list(range(1,10))
print(L)
def f(x):
	return x*x

L1=list(map(f,L))
print(L1)

L2=[]
for n in L:
	L2.append(f(n))
print(L2)

#reduce
from functools import reduce
num=[1,3,5,7,9]
def add(x,y):
	return x+y

print(reduce(add,num))
print(sum(num))

def fn(x,y):
	return x*10+y

print(reduce(fn,num))

#写一个str2num的方法，相当于int(str)
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2num(s):
	def fn(x,y):
		return x*10+y
	def char2num(ch):
		return DIGITS[ch]
	return reduce(fn,map(char2num,s))

print(str2num('13579'))

#使用lambda简化
def char2num(ch):
	return DIGITS[ch]

def str2num(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2num('12345'))

#practice
def normalize(name):
	if len(name) !=0:
		s=name.lower()
		s1=ord(s[0])
		s1=s1-32
		s2=chr(s1)
		s3=s2+s[1:]
		return s3
	else:
		return None

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#practice2
def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,L)

#测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('success!')
else:
    print('fail!')

#practice3
def str2float(s):
	def f1(x,y):
		return x*10+y
	def f2(x,y):
		return x*0.1+y
	def char2num(ch):
		return DIGITS[ch]
	i=0
	while i<len(s):
		if s[i]=='.':
			break
		i=i+1
		
	s1=s[:i]
	s2=s[i+1:]
	s2=s2[::-1]+'0'
	return reduce(f1,map(char2num,s1))+reduce(f2,map(char2num,s2))

#测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('success!')
else:
    print('fail!')
 
 