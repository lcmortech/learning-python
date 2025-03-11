# A program to convert celsius temps to Farenheit

def main():
	cels = int(input("Please enter a value in celsius"))
	conv_num = (9 / 5) * (cels + 32)
	print(f"{cels} is {conv_num} in Farenheit")
	
main()
