# -*- coding=utf-8 -*-

print(ord('a'))
print(ord('中'))

print(chr(66))
print(chr(25991))

print(b'abc')
print('abc'.encode('ascii'))
print(b'acd'.decode('ascii'))

print(len('acc'))

print('Hello, %s' % ('Calmer'))
print('Hi,%2d-%02d' % (3,1))
print('%.2f %%' % (27.625))

print('Hello,{0},rate up to {1:.2f}%'.format('Calmer',38.956))

#practice
s1=72
s2=85
r=(s2-s1)/s1
print('%.1f%%' % r)
print('{0:.1f}%'.format(r))