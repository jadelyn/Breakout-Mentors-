
def sum_square_difference(start, end): 
	return square_of_sum(start,end) - sum_of_square(start,end)


def square_of_sum(start,end): 
	sum = 0 
	for i in range(start, end+1): 
		sum = sum + i 
	return sum**2

def sum_of_square(start,end): 
	sum = 0 
	for i in range(start, end+1): 
		sum = sum + i**2 
	return sum 

print(sum_square_difference(1,100))
