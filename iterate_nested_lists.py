list = ['a', ['b', ['c', ['d']], 'e'], 'f'] 

# iterate over a list with nested values 
def nested_loops():
    for x in list:
        for y in x:
            for z in y:
                for l in z:
                    print(l)

#recursive method
def iterate_recursively(list):
    for x in list:
        while isinstance(x, str):
            print(x)
        else:
            iterate_recursively(x)

iterate_recursively(list)
