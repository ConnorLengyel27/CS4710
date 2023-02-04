for i in range(5): #for loop that iterates 5 times
    for j in range(i+1): #for loops that iterates through the range of i
        print('*', end=' ') #prints * in line
    print() #prints new line
count = 4 #count variable 
for i in range(4): #for loop that iterates four times
    for j in range(count): #for loop that iterates through the range of count
        print('*', end=' ') #prints * in line
    print() #prints new line
    count -= 1 #subtracts 1 from count
