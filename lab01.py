import argparse as ap
import random
import numpy as np

#PART 1
def Sort(values):
	for i in range(len(values)):
		for num in range(0, len(values) - i - 1):# nested for loop so it will always interate all the way the end of the array
			if values[num] > values[num + 1]:
				buffer = values[num] # swapping the values of the numbers if the current number is bigger than the one ahead
				values[num] = values[num + 1]
				values[num + 1] = buffer
	
	return values


#PART 2
def Search(sorted_values, query):
	right = len(sorted_values) - 1
	left = 0 # declare pointers to narrow doen where the quary could be
	current = right // 2
	comparisons = 0

	while right >= left: # keep comparing until the pointers pass each other
		comparisons += 1
		if sorted_values[current] == query:
			return sorted_values[current], current, comparisons
		elif sorted_values[current] < query:
			left = current + 1
		else:
			right = current - 1
		
		if right >= left:
			current = (left + right) // 2

	# quary was not found in the array

	left = len(sorted_values) - 1 if left >= len(sorted_values) else left # need to make sure the left pointer does not go out os index
	# dont need to do it with right pointer because -1 will not be out of index and will just equal the last index


	if abs(query - sorted_values[right]) < abs(sorted_values[left] - query): # finding which pointer is closer to the value of the query
		index = right
	else:
		index = left
	return sorted_values[index], index, comparisons


# main function
def main():

	# Parser to read input from the command line.
	# Notice the import at the top of this file
	# In the example below, you read an integer passed through the command line
	# as follows: python lab01-template --test 10
	# You need to search online how to read multiple integers instead of just one
	# like I did in this example
	parser = ap.ArgumentParser()
	parser.add_argument('--MyArray', type=int, required=False, nargs='+')#allows for use of command line arguments
	args = parser.parse_args()

	

	
	my_test_value = np.array(args.MyArray, dtype=int)
	my_test_value = my_test_value[(my_test_value >= 0) & (my_test_value <= 99)] # assign the inputed values to the variable and remove the numbers that are outside of the bounds

	if my_test_value.size == 0: # if it is still empty, we fill it with random numbers
		my_test_value = np.random.randint(0, 100, size=10, dtype=int)

	# Uncomment and use the two lines below to sort & print the vector as required in Part 1
	sorted_array = Sort(my_test_value) # calling the sort function
	print(sorted_array)



	query =random.randint(0, 99) # generating a random query
	match, idx, n_sim = Search(sorted_array, query) #finding the value in the array that is closest to the query and also returning its value, index, and 



	# Uncomment and use the two lines below to print the output of Part 2
	print("Looking for query: {}".format(query))
	print("Best match is {} in position {}. I performed {} sim checks".format(match, idx, n_sim))


# This is how you launch your main function.
if __name__ == "__main__":
    main()