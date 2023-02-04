my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #list to store numbers
index = 0 #variable for index of list
for i in my_list: #for loop to iterate through list
    if index % 2 != 0: #if statement that checks if the number is even or odd
        print(my_list[index]) #prints number
    index += 1 #adds 1 to index
