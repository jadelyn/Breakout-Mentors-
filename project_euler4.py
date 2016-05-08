def is_palindrome(num): 
	num_str = str(num)
	for i in range(0, len(num_str) / 2): 
		if num_str[i] != num[len(num_str) - 1 - i]: 
			return False
	return True 


def find_largest_palindrome(): 
	all_palindromes = [] 
	for i in range(100, 1000): 
		for j in range(i, 1000): 
			product = i * j 
			if is_palindrome(product): 
				all_palindromes.append(product)

	return max(all_palindromes)



print(find_largest_palindrome()t)

