un_list = ['alice','brian','candace'] #未验证列表用户
yn_lists = [] #空列表

while un_list: #循环不断运行，知道un_list变为空的
	tan = un_list.pop() #列表末尾删除未验证的用户，存储到变量tan

	print("Verifying user: " + tan.title()) #打印正在验证的用户
	yn_lists.append(tan) #将用户加入到验证列表中

print("\nThe following users have been confirmed:") #再打印以验证用户
for yn_list in yn_lists:
	print(yn_list.title())