class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.age = 0

	def get_zhi(self):
		lon_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return lon_name

	def get_message(self):
		print("lichengbiaosudu " + str(self.age) + " namekuai!")

	def get_pan(self,panduan):
		if age <= panduan:
			self.age = panduan
		else:
			print("no")
	def get_xiugai(self,moinse):
		self.age += moinse

my_new_car = Car('Audi','A4',2017)
print(my_new_car.get_zhi())

my_new_car.get_xiugai(-1)
my_new_car.get_message()