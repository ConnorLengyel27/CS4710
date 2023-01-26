N = int(input("How many students are there? ")) #user input for number of students
lbs = [] #empty list to store student weights in pounds
for i in range(N): #for loop for user input of student weights
    lbs.append(int(input("Please enter the weight of the student ")))
kg = [] #empty list to store student weights in kilograms
for i in lbs: #for loop to convert weights from pounds to kilograms
    kg.append(i * 0.45359237)
print(kg) #prints weights in kilograms
