numbers_map = {1: "one", 2: "two", 3: "three", 4:"four", 5:"five", 6:"six", 7:"seven",8:"eight", 9:"nine", 10:"ten", 11: "eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15: "fifteen", 16: "sixteen", 17:"seventeen",	18: "eighteen", 19: "nineteen", 20: "twenty", 30:"thirty",40:"forty",50:"fifty", 60:"sixty",70:"seventy",80:"eighty",90:"ninety", 1000: "onethousand"}


def number_letter_counts(): 
	num_letters = 0 q

	for i in range(1,1001): 
		str_num = str(i)
		print(i)

		if i in numbers_map: 
			num_letters += len(numbers_map[i])
		else: 
			num_digits = len(str_num)

			if num_digits == 2: 
				num_letters += count_two_digits(str_num)

			elif num_digits == 3:
				first_char = str_num[0]
				num_letters += len(numbers_map[int(first_char)])
				num_letters += len("hundred") 
				second_char = str_num[1]
				if second_char != "0": 
					num_letters += len("and")
					num_letters += count_two_digits(str_num[1:])
				else:

					third_char = str_num[2]
					if third_char != "0":
						num_letters += len("and")

						num_letters += len(numbers_map[int(third_char)])


	return num_letters

def count_two_digits(n):
	num_letters = 0

	if int(n) in numbers_map: 
		num_letters += len(numbers_map[int(n)])
	else: 


		first_char = n[0]
		num_letters += len(numbers_map[int(first_char+"0")])

		second_char = n[1]
		num_letters += len(numbers_map[int(second_char)])

	return num_letters 


print(number_letter_counts())
