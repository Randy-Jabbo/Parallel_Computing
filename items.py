import numpy as np


def PrepareBag(items, bag_size, index = None):
    item = np.array(items[0])
    value = np.array(items[1]).astype(int)
    size = np.array(items[2]).astype(int)
	
    if index is None: # once the function is first called and index does not have a value it sets it to the last items index
        index = len(item) - 1 
	
    if index < 0: # base case/ when the funciton ends.
        return [], 0, 0
    
    pass_item, pass_value, pass_size = PrepareBag(items, bag_size, index - 1) # the branch where this item is excluded

    if size[index] <= bag_size: # if this item fits in the bag, we run the branch of including it
        take_item, take_value, take_size = PrepareBag(items, bag_size - size[index], index - 1)
        take_value += value[index]
        take_item += [item[index]]
        take_size += size[index]
    
        if take_value > pass_value: # check if its more effective to have this value rather then pass on it.
            return take_item, take_value, take_size
    
    return pass_item, pass_value, pass_size # if its more effective to leave this item behind we return these values


def main():
	items = np.array( [["ring", "pen", "watch", "laptop", "earrings"], [130, 4, 50, 250, 80], [3, 2, 7, 14, 2]] )
	bag_size = 15

	object_names, tot_val, tot_size = PrepareBag(items, bag_size)

	print("Inputs")
	print(items)
	print("Bag size: {}".format(bag_size))
	print()
	print("Outputs")
	print("Object Names: {}".format(object_names))
	print("Total Value: {}".format(tot_val))
	print("Object Names: {}".format(tot_size))

if __name__ == "__main__":
    main()