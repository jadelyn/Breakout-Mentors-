def find_nth_prime_number(n): 
	counter = 0 
	num_to_check = 1

	while counter <= n: 
		is_prime = True 
		for i in range(2,int(pow(num_to_check,1/2)) + 1): 
			if num_to_check % i == 0: 
				is_prime = False 
				break 

		if is_prime: 
			counter += 1 

		num_to_check += 1 

	return num_to_check-1


# print(find_nth_prime_number(9))

print(find_nth_prime_number(10001))







