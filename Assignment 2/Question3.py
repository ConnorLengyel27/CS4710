x = [23, "Python", 23.98] #list storing different data
print(x) #prints the list
newList = []
for i in x: #for loop that iterates through the loop and prints the type of each variable
    newList.append(type(i))
print(newList)
