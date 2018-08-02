#切片
#循环法截取
L=['calmer','pinger','springer','good','nice']

r=[]
n=3
for i in range(n):
	r.append(L[i])
print(r)

#切片
print(L)
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

L=list(range(1,101))  #产生1~100的数
print(L[:10])		  #取前10个数
print(L[-10:])		  #取后10个数
print(L[10:20])		  #取10~20个数
print(L[:10:2])		  #在前10个数中，每两个取一个数
print(L[::5])		  #在所有数中，每5个取一个数

#字符串的截取
s='ABCDEFGH'
print(s[:3])
print(s[::2])

#去掉字符串首尾的空格可以用strip()实现
def trim1(s):
	font=0
	for n in s:
		if n!=' ':
			break
		font=font+1

	tail=-1
	while tail>-len(s):
		if s[tail]!=' ':
			break
		tail=tail-1
	return s[font:(len(s)+tail+1)]

#递归实现
def trim(s):
	if s[:1]!=' 'and s[-1:]!=' ':
		return s
	elif s[:1]==' ':
		return trim(s[1:])
	elif s[-1:]==' ':
		return trim(s[:-1])
# 测试:
if trim('hello  ') != 'hello':
    print('fail1!')
elif trim('  hello') != 'hello':
    print('fail!2')
elif trim('  hello  ') != 'hello':
    print('fail!3')
elif trim('  hello  world  ') != 'hello  world':
    print('fail!4')
elif trim('') != '':
    print('fail5!')
elif trim('    ') != '':
    print('fail6!')
else:
    print('success!')	
