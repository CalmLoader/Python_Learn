#迭代器
from collections import Iterable
from collections import Iterator
print('first:')
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x*x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

print('\nsecond:')
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((x*x for x in range(10)),Iterator))
print(isinstance(100,Iterator))

print('\nthird:')
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))
print(isinstance((x*x for x in range(10)),Iterator))
print(isinstance(100,Iterator))

