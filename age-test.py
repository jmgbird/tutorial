#install package
a = int(input("How old are you , "))
print(a)
if a in range(1, 20):
	print('You are too young, go home')
elif a in range(21, 60):
	print('You are able to drink')
	print("access key = AKIA98084358485748745")
elif a in range(61, 1050):
	print('You are too old, go home')
else:
	print('You aren''t born')


