import numpy as np

def BinSearch(MySortedVec, Query):
	length = len(MySortedVec)
	current = length // 2
	if (MySortedVec(current) == Query):
		return 
	
	

def PrepareBags(items, bag_size):
    pass

def Sort(values):
	for i in range(len(values)):
		for num in range(0, len(values) - i - 1):# nested for loop so it will always interate all the way the end of the array
			if values[num] > values[num + 1]:
				buffer = values[num] # swapping the values of the numbers if the current number is bigger than the one ahead
				values[num] = values[num + 1]
				values[num + 1] = buffer
	
	return values


def main():
    pass