'''
Arrays-container that hold fixed number of items of same type

structure
array(typecode, [intializers])
'''

from array import *
array1 = array('i', [10,20,30,40,50])

#tranverse array
for x in array1:
    print(x)

#access array element - this is done by index
print(array1[2])

# insertion into array 
array1.insert(1,80)
print(array1)

# delete from array 
array1.remove(80)
for x in array1:
    print(x)

# search through array 
print(array1.index(50))
