import sys
print(sys.float_info.epsilon)

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a-b)
if abs(a-b) < sys.float_info.epsilon:
	print("a와 b는 같은 값")
else:
	print("a와 b는 다른 값")