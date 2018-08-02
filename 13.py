#1位置参数 默认参数

#必选参数在前，默认参数在后
print('\nfirst:')
def mypow(x,n=2):
	s=1
	while n>0:
		n-=1
		s*=x
	return s

print(mypow(2))
print(mypow(2,4))

#一个致命坑
def add_end(L=[]):
	L.append('END')
	return L

print(add_end())
print(add_end())

#所以默认参数一定要指向不变对象

#修改以上例子,直接进行了函数重写

def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

print(add_end())
print(add_end())



#2可变参数
print('\nsecond:')
#计算a^2+b^2+c^3+...
def cal(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

#调用
print(cal())
print(cal(1,2,3))
list=[1,2,3]
print(cal(list[0],list[1],list[2]))
print(cal(*list))


#3关键字参数
print('\nthird:')
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

#调用
person('calmer',21)

person('calmer',21,city='chengdu',career='student')

extra={'major':'computer science','city':'chengdu'}
person('calmer',21,**extra)



#4命名关键字参数
#不能限制
print('\nfourth:')
def person2(name,age,**kw):
	if 'city' in kw:
		print('city exit!','city:',kw['city'])
	if 'job' in kw:
		pass
		print('job exit','job:',kw['job'])
	print('name:',name,'age:',age,'other:',kw)
#调用
person2('calmer',21,city='chengdu')
person2('calmer',21,city='chengdu',job='Engineer')

#限制
def person3(name,age,*,city='hangzhou',job):
	print(name,age,city,job)

#调用，此处必须加上命名关键字参数的名字，否则调用错误
person3('calmer',21,city='chengdu',job='Game Engineer')
person3('calmer',21,job='Game Engineer')

def person4(name,age,*args,city,job):
	print(name,age,args,city,job)
#调用
person4('calmer',21,2,3,1,city='chengdu',job='Game Engineer')

#5参数组合
print('\nfivth:')
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c',c,'d=',d,'kw=',kw)

#调用
f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',d='d',f='f',x=99)
f2(1,2,d=99,ext=None)

args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)


#practice
def product(*numbers):
	if len(numbers)!=0:
		mul=1
		for n in numbers:
			mul=mul*n
		return mul
	else:
		raise TypeError('No params')

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('fail!')
elif product(5, 6) != 30:
    print('fail!')
elif product(5, 6, 7) != 210:
    print('fail!')
elif product(5, 6, 7, 9) != 1890:
    print('fail!')
else:
    try:
        product()
        print('failed!')
    except TypeError:
        print('success!')
