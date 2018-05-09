class Dog():
	def __init__(self,name,age):
		#可通过实例访问的变量叫属性
		self.name = name #获取储存在形参name中的值，并将其存储在变量name中，然后该变量被关联到当前创建的实例
		self.age = age

	def sit(self):
		print(self.name.title() + "is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

#创建实例
my_dog = Dog('willie',6)
your_dog =Dog('lucy',3)
#调用方法
my_dog.sit()
my_dog.roll_over()
print("My dog'sname is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + "years old.")
your_dog.sit()