class Car():
#定义方法
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		#创建一个初始值总为0的属性
		self.odometer_reading = 0

	def get_descriptive_name(self):
		'''返回整洁的描述性信息'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name

	def read_odometer(self):
		#读取汽车的里程表
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odmeter(self,mileage):
		'''

		'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("NO!")
#接受一个单位为英里的数字，将其加入到self.odometer_reading
	def increment_odometer(self,miles):
		'''将里程表数增加指定的量'''
		self.odometer_reading += miles

class ElectricCar(Car):
	def __init__(self,make,model,year):
		'''初始化父类属性'''
		#帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar的父类的方法__init__()  ，让ElectricCar包含父类的所有属性
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def fill_ags_tank():
		print("This car doesn'tneed a gas tank!")




#实例
my_used_car = Car('audi','A4',2016)
my_tesla = ElectricCar('telsa', 'models', 2016)

print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()


print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


