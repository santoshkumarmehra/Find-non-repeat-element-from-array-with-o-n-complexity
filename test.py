str=["santosh","nobita","ban10","kick","himalayan","awesome"]
max=0
index=0
for i in range(0,len(str)):
	if len(str[i])>max:
		max=len(str[i])
		index=i
print("\n","max length of character = ",str[index])
print("\n","max character in single string = ",index)