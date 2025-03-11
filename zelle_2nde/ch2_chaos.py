# A simple program illustrating chaotic behavior


def main():
	print("This program illustrates a chaos function")
	x = float(input("Enter a number between 0 and 1: "))
	for i in range(5):
		print(i * i)
		
	for d in [3,1,4,1,5]:
		print(d, end=" ")
		print(d, sep= ",")
		
	for i in range(4):
		print("Hello")
	
	for i in range(5):
		print(i, 2**i)

main()

print("start")
for i in range(0): # prints once
	print("Hello")
print("end")
