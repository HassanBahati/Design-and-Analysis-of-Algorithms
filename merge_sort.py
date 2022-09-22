# Merge Sort - works like binary search - split problem into sub problems 
# 1 start with unsorted list 
# 2 split the list into 2 sub lists
# 3 keep spliting evenly until 1 element lists are attained 
# 4 work backwards 
# 5 repeatedly merge single element lists and sort them 

# naively sorting - passing a 1 element list to a merge sort 


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublist created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)



def split(list):
    """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list) // 2

    left = list[:mid] 
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges 2 lists, sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1


    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l




def verify_sorted(list):
    n = len(list)

    if n ==0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])