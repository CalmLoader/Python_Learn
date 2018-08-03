#迭代
from collections import Iterable
#1
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)

for key in d.values():
	print(key)

for key,value in d.items():
	print(key,value)

for ch in 'ABC':
	print(ch)

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

for i,value in enumerate(['x','y','z']):
	print(i,value)

for x,y in [(1,1),(2,2),(2,3)]:
	print(x,y)

#practice
def findMinAndMax(L):
	if len(L) !=0:
		L.sort()
		return L[0],L[-1]
	else:
		return(None,None)


#print(findMaxAndMin([13,2,1,4,5,2]))

# 测试
if findMinAndMax([]) != (None, None):
    print('fail1!')
elif findMinAndMax([7]) != (7, 7):
    print('fail2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('fail3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('fail4!')
else:
    print('success!')