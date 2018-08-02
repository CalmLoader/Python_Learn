#dict:key-value
#names=['calmer','good','nice']
#scores=[100,98,88]
d={'calmer':100,'good':98,'nice':88}
print(d['calmer'])
d['fi']=85
d['ff']=78
print(d['fi'])
print(d)

#判断key是否在d内
print('fi' in d)

#删除一个key
d.pop('fi')
print(d.get('hh',-1))

#set

s=set([1,2,3])
print(s)

s=set([1,1,2,3,4,5,3])
print(s)

s.add(6)
s.remove(1)
print(s)

s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)

d={1:'good',2:'nice',3:'bad'}
x=input('Please enter your key')
x=int(x)
print(d[x])

#
alp=['b','c','a']
alp.sort()
print(alp)
a='abc'
print(a.replace('a','A'))