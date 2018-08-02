#list
print('list:')
classmates=['abc','def','xyz']
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.append('ok')
classmates.insert(1,'calmer')
print(classmates)
classmates.pop()
classmates.pop(0)
classmates[0]='good'
print(classmates)

L=[]
len(L)

#tuple
print('tuple:')
t=(1,2)
print(t)

#长度为1的tuple
q=(1,)
print(q)
#’可变的‘ tuple
t=('a',True,['b','c'],23)
print(t)
t[2][0]=False
print(t)

#practice
L = [
	['Apple','Google','Microsoft'],
	['Java','Python','Ruby','C/C++'],
	['calmer','jiujiu','good']
]

print('''%s
%s
%s
''' %(L[0][0],L[1][1],L[2][0]))

print(L[0][0]+'\n'+L[1][1]+'\n'+L[2][0])
