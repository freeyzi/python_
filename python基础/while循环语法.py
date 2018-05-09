#active = True
#while active:
#	message = input("2333.")
#
#	if message == 'quit':
#		active = False
#	else:
#		print(message)

#要立即退出while 循环，不再运行循环中余下的代码，
#也不管条件测试的结果如何，可使用break语句。
#break 语句用于控制程序流程，可使用它来控制哪些代码行将执行，
#哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
#while True:
#	city = input("23333")
#
#	if city == 'quit':
#		break
#	else:
#		print("NO!" + city.title() + "!")
#要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue 语句，
#它不像break 语句那样不再执行余下的代码并退出整个循环。
current = 0
while current < 10:
	current += 1

	if current % 2 == 0:
		continue
	print(current)


