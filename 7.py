#条件判断
# -*- coding=utf-8 -*-
age = input('Please input your age : ')
age = int(age)
if age>=18:
	print('your age is',age)
	print('adult')
elif age>=6:
	print('your age is',age)
	print('teenager')
else:
	print('kid')

#practice

height=1.75
weight=80.5
bmi=weight/(height*height)

if bmi<18.5:
	print('more low')
elif bmi<25:
	print('normal')
elif bmi<28:
	print('fat')
elif bmi<32:
	print('a little fat')
else:
	print('too much fat')