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

class Battery():

	def __init__(self,battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can approximately " + str(range)
		message += "miles on full charge."
		print(message)


class ElectricCar(Car):
	def __init__(self,make,model,year):
		
		#帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar的父类的方法__init__()  ，让ElectricCar包含父类的所有属性
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		self.battery = battery()

	def fill_ags_tank():
		print("This car doesn'tneed a gas tank!")


#实例

my_tesla = ElectricCar('telsa', 'models', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


