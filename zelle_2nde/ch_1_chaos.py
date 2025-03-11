# A simple program illustrating chaotic behavior


def main():
	print("This program illustrates a chaos function")
	#x = float(input("Enter a number between 0 and 1: "))
	num = int(input("How many times do you want to run this program?"))
	x = 2
	for _ in range(num):
		#x = 3.9 * x * (1 - x)
		#x = 3.9 * (x - x * x)
		x = 3.9 * x - 3.9 * x * x
		print(x)1
		
main()
