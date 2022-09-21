# STEPS
# 1 determine the middle of a sorted list
# 2 compare element at middle position to target, 
# 3 if middle value matches target, return middle position and terminate
# 4 if doesnt match, check if element in middle position is smaller than target
# 5 if element in middle position is smaller than target, go to step 2 with new list that starts at middle position to the end of list
# 6 if element in middle position is bigger than target, go to step 2 with new list that starts from beginning of list to the moddle position
# 7 repeat until sublist contains 1 element or targt is found
# 8 if sublist doesnt contain the element. end as target doesnt exist 

# Input - sorted list 
# Output - position of target value, or value to show it doesnt exist

# time complexity - O(log n) because the size is split by half everyother time
# best case is O(1) when the value is at middle position