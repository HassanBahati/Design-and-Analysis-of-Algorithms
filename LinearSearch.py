# linear search - sequential search or simple search

# STEPS
# 1 start at beginning of sorted/unsorted list 
# 2 compare current value and target value
# 3 if current value is target, return current value and terminate
# 4 if current value is not target, move to next value 
# repeate step 2

# Input - set of sorted/unsorted values 
# Output - value that matches one being looked for 

# time complexity - O(n)

def linear_search(list, target):
    """
    returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None



def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]

