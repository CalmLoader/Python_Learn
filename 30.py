#面向对象编程

class Student(object):
	"""docstring for Student
"""
	def __init__(self, name,score):
		self.name=name     #都是公有变量，可以外部直接访问
		self.score=score

	def print_score(self):
		print('%s,%s' % (self.name,self.score))

bart=Student('Bart Simpson',60)
lisa=Student('Lisa Simpson',90)

bart.print_score()
lisa.print_score()


#访问限制，区别公有变量和私有变量
#私有变量传参时候可以检查参数的有效性


class Student2(object):
	"""docstring for Student2"""
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def get_name(self):
		return self.__name

	def set_name(self,name):
		self.__name=name

	def get_score(self):
		return self.__score

	def set_score(self,score):
		self.__score=score


bart=Student2('Bart Simpson',60)
lisa=Student2('Lisa Simpson',90)

print(bart.get_name(),bart.get_score())
bart.set_score(88)
print(bart.get_name(),bart.get_score())


