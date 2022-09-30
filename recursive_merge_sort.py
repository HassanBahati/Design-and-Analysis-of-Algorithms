def merge_sort(arr):

    if len(arr) <= 1:
        #Best Case
        return arr
    
    #recussive case
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    print(len(arr))
    print(left)
    print(right)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(right,left)


# def merge(left,right):




arr= [90,10,20,100,1000]

print(merge_sort(arr))
