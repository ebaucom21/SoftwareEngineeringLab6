
# Main Function
if __name__ == "__main__":
	encoded = None
	while (True):
		menu()
		option = int(input("Please enter an option: "))
		match option:
			case 1:
				# Option 1
				password = int(input("Please enter your password to encode: "))
				encoded = encode(password)
				print("Your password has been encoded and stored!")
				print()
			case 2:
				# Option 2
				# To be implemented
				decode()
			case default:
				break



# Menu function to print initial user menu
def menu():
	print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n)


# Encode function that moves all digits up 3
def encode(num):
	fin = ""
	st = str(num)
	for i in range(len(st)):
		temp = int(st[i])+3
		fin += str(int%10)
	return int(fin)


# Decode function that moves all digits down by 3
# To be implemented
def decode(num):
	return 0
