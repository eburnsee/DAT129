
def create_icon():
	print("Hello and welcome. You may use this program to display your icon.\nYou will be prompted to enter ten lines of TEN ones and zeros.")
	row_name_list = ["one", "two" , "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
	row_list=[]
	# loop through all ten rows
	for row in row_name_list:
		# get input for each row
		row_input = input("Please enter ten characters (zeros and ones only, please!) for row " + row + ": ")
		# test to see if each row is 10 characters long
		if len(row_input) == 10:
			row_input_list=list(row_input)
			# test to see if each character is a 1 or a 0
			for inp in row_input_list:
				if (inp != "0") and (inp != "1"):
					print("You failed to enter ONLY ten ones and zeros. Please try again.")
					# restart the program if the test fails
					create_icon()
				else:
					continue
			# if both tests pass, the input will be saved into row_list
			row_list.append(row_input)
		else:
			print("You failed to enter ten ones and zeros. Please try again.")
			# if the length test fails, restart the program
			create_icon()
	# see if the user would like to scale the icon
	scaled_rows = input("Would you like to scale your icon? (yes/no)")
	if scaled_rows.lower() == "yes":
		print("Thinking")
	elif scaled_rows.lower() == "no":
		# print the icon
		for row_inp in row_list:
			print(row_inp)



create_icon()
	


