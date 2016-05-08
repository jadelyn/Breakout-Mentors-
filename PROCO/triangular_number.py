def divisible_triangle_number():
	n = 1
	while (1): 
		num_factors = find_num_factors(n)
		print(num_factors)

		if num_factors > 500:
			break
		else: 
			n += 1
	return (n**2 + n)/2
		


# Return number of factors that the nth triangle number has 
def find_num_factors(n): 
	triangle = (n**2 + n)/2 
	i = 1
	num_factors = 0 
	while i <= triangle: 
		if triangle % i == 0: 
			num_factors += 1
		i += 1 
	return num_factors 




print(divisible_triangle_number())

# print(find_num_factors(1))
# print(find_num_factors(2))
# print(find_num_factors(3))


