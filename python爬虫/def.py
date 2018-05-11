#TempStr = input("请输入带有符号的温度值：")
#if TempStr[-1] in ['F','f']:
#	C = (eval(TempStr[0:-1]) - 32)/1.8
#	print("转换后的温度是{:.2f}C".format(C))
#elif TempStr[-1] in ['C','c']:
#	F = 1.8*eval(TempStr[0:-1]) + 32
#	print("转换后的温度是{:.2f}F".format(F))
#else:
#	print("格式输入错误")

#s = "PYTHON"
#while s != "":
#	for c in s :
#		print(c, end="")
#	s = s[:-1]

#s = "PYTHON"
#while s != "":
#	for c in s :
#		if c == "T":
#			break
#		print(c,end="")
#	s = s[:-1]

#for c in "PYTHON":
#	if c == "T" :
#		continue
#	print(c, end="")
#else:
#print("正常退出")

for c in "PYTHON":
	if c == "T":
		break
	print(c,end="")
else:
	print("正常退出")