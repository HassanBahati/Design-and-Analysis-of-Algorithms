def nested_linear_search(mylist, val):

    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            #print i,j
            if mylist[i][j] == val:
                return print(mylist[i])

    return str(val) + ' not found'



nested_linear_list = [[1,2,3],[5,6,7],[9,10,11]]

nested_linear_search(nested_linear_list, 1)

