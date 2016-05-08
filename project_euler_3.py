import math
def largest_prime_factor():
	curr = 2
	max_prime = 2
	while curr <= int(math.sqrt(600851475143)) + 1: 
		if is_prime(curr): 
			max_prime = curr
			print(str(max_prime))
		curr += 1
	return max_prime 


def is_prime(n):
	i = 2
	while i <= int(math.sqrt(n)): 
		if n % i == 0: 
			return False
		i += 1 
	return True

print (largest_prime_factor())
# assert is_prime(5) == True
# assert is_prime(7) == True
# assert is_prime(11) == True
# assert is_prime(13) == True
# assert is_prime(28) == False