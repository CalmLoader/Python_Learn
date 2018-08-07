#filter
def is_odd(n):
	return n%2==1

L=list(range(10))

print(list(filter(is_odd,L)))

L1=['A','','B',None,'C',' ']

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,L1)))

def odd_iter():
	n=1
	while True:
		n=n+2
		yield n

def not_divisible(n):
	return lambda x:x%n>0

def primes():
	yield 2
	it=odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(not_divisible(n),it)

for n in primes():
	if n<1000:
		print(n)
	else:
		break

print('\npractice:\n')
#practice
def is_palindrome(n):
	orgin=str(n)
	ch=orgin[::-1]
	if orgin==ch:
		return True
	else:
		return False


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('success!')
else:
    print('fail!')



#sorted

L=[26,-45,23,-15,60]
print(sorted(L))

print(sorted(L,key=abs))

SL=['bob','about','Zoo','Credit']
print(sorted(SL))

print(sorted(SL,key=str.lower))

#翻转
print(sorted(SL,key=str.lower,reverse=True))

#practice
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
	return t[0]

#测试
L2 = sorted(L, key=by_name)
print(L2)

#practice
def by_score(t):
	return t[1]

L2 = sorted(L, key=by_score,reverse=True)
print(L2)