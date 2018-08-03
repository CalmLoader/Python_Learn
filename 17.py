#列表生成式
import os
print(list(range(1,11)))
L=[]
for x in range(1,11):
	L.append(x*x)
print(L)

L=[x*x for x in range(1,11)]
print(L)

#仅偶数的平方
L=[x*x for x in range(1,11) if x%2==0]
print(L)

#全排列
L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)

#列出当前目录下的所有文件和目录
L=[d for d in os.listdir('.')]
print(L)

d={'a':1,'b':2,'c':3}
L=[k+'='+str(v) for k, v in d.items()]
print(L)

s=['Hello','World','IBM','Apple']
L=[n.lower() for n in s]
print(L)

#practice

s=['Hello','World','IBM','Apple',18,None]
L=[n.lower() for n in s if isinstance(n,str) ]
print(L)