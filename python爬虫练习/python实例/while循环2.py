active = True
while active:
	message = input("(quit)exit!")
	if str(message) == 'quit':
		break
	if int(message) <= 3:
		print("0$")
	elif int(message) >3 and str(message) <= 12:
		print("10$")
	else:
		print("15$")