#organise related data in sublist nested in the parent list 
mumbled_data = [
["KATUKUNDA Rochelle","A94169","S21B23/016"],
["NAJJOBA Tracy","A95681","S21B23/034"],
["MUGANGA Charles","A96447","J22B23/032"],
["NKATA Joshua Luyombya","A94161","S21B23/008"],
["MUKISA Isaiah","A94160","S21B23/007"],["Afghanistan","93"],
["Tiji","679"],["Bahamas","1-242"],["Tanzania","255"],
["Saint Vincent and the Grenadines","1-784"],["Ukraine","380"]
]


def search(list, target):
    for i in list: # i is sub-lists in the parent list
        for j in i:# j is each item in sub-list
            if target == j:
                return i      #return all related data to search query
    
    return "Not found"  #return not found if item doesnt exist



#search for country code "7"
print(search(mumbled_data,"7"))

#search for access number of a student that is A94160
print(search(mumbled_data,"A94160"))

#search for a country code 380
print(search(mumbled_data,"380"))

#search for a student called Doe
print(search(mumbled_data,"Doe"))

