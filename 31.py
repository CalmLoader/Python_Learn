#继承与多态
#继承

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def eat(self):
		print('dog is eating food')

class Cat(Animal):
	pass

dog=Dog()
cat=Cat()

dog.run()
cat.run()

dog.eat()


#多态

class Dog2(Animal):
	def run(self):
		print('dog is running...')

class Cat2(Animal):
	def run(self):
		print('cat is running...')

dog=Dog2()
cat=Cat2()

dog.run()
cat.run()

#判断是否
a=list()
b=Animal()
c=Dog()

print(isinstance(b,Animal),isinstance(c,Dog),isinstance(b,Dog),isinstance(c,Animal))


#