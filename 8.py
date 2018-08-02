#循环

#用于数组遍历的数组
names=['calmer','good','nice']
for name in names:
	print(name)
print('\n')

for index in range(len(names)):
	print(names[index])
print('\n')

#Python这个字符串中的每一个字母输出
for letter in 'Python':    
   print('当前字母:',letter)

#计算1+2+3...+100 ,
print(list(range(3)))

sum=0
for x in range(101):
	sum = sum + x
print(sum)

#for i from 1 to 100:
for i in range(1,101):
	print('ss')

#while循环
sum=0
n=100
while n>0:
	sum+=n
	n-=1
print(sum)

#break  continue
n=0
while n<=100:
	n=n+1
	if n>10:
		break
	if n%2==0:
		continue
	print(n)
print('END')