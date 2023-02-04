list1 = [1,2,3,3,3,3,4,5] #sample list
list2 = [] #new list
for i in list1: #for loop to iterate through sample list
    if i not in list2: #checks if number is in list2
        list2.append(i) #appends number to list2
print(list2) #prints list 2
