import statistics #import statistics for median function
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #list of ages
ages.sort() #sorts ages
min = ages[0] #gets lowest age
max = ages[-1] #gest highest age
ages.append(min) #adds lowest age to end of list
ages.append(max) #adds highest age to end of list
median = statistics.median(ages) #gets median of list
avg = 0 #variable to calculate average
for i in ages: #for loop that adds each age to avg
    avg += i
avg = avg / len(ages) #divides avg by number of items in list
range = max - min #calculates range of ages
#prints all data
print(ages)
print(min)
print(max)
print(median)
print(avg)
print(range)
