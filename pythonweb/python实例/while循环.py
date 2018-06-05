responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
	#提示输入名字和回答
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	#将答案问卷放在字典中
	responses[name] = response
	#看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond? (yes/no)")
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name,response in responses.items():
	print(name + " would link to climb " + response + ".")