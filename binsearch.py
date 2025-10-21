
import numpy as np
import argparse as ap



def BinSearch(sorted_values, query, left=0, right=None, checks = 0):

    if left > right:  # query not found, find closest value
        # making sure the left and right pointers in within the bounds
        if right < 0:
            return sorted_values[0], 0, checks
        if left >= len(sorted_values):
            return sorted_values[-1], len(sorted_values) - 1, checks
        
        if abs(query - sorted_values[right]) <= abs(sorted_values[left] - query):# compared which side is closer to the quaryand returns it
            return sorted_values[right], right, checks
        else:
            return sorted_values[left], left, checks
    
    current = (left + right) // 2
    checks += 1 # increment checks for each iteration we need to test a value
    
    if sorted_values[current] == query: # quary found as one of the values in array
        return sorted_values[current], current, checks
    elif sorted_values[current] < query: # querry is in the top half
        return BinSearch(sorted_values, query, current + 1, right, checks)
    else: # last case, query is in bottom half
        return BinSearch(sorted_values, query, left, current - 1, checks)


def sort(values):
	for i in range(len(values)):
		for num in range(0, len(values) - i - 1):# nested for loop so it will always interate all the way the end of the array
			if values[num] > values[num + 1]:
				buffer = values[num] # swapping the values of the numbers if the current number is bigger than the one ahead
				values[num] = values[num + 1]
				values[num + 1] = buffer
	
	return values

def main():
      
	parser = ap.ArgumentParser()
	parser.add_argument('--values', type=int, required=True, nargs='+')# gets the array of values from command line
	parser.add_argument('--query', type=int, required=True)# gets the quary from the command line
     
	args = parser.parse_args()
    
	values = np.array(args.values)
	query = args.query
     
	sorted_values = sort(values)
	length = len(sorted_values)


    
	val, idx, nsim = BinSearch(sorted_values, query, 0, length - 1)
	print(val, idx, nsim)
	


if __name__ == "__main__":
    main()