userInput = input("please enter a string") #user input for string
lowercase = 0 #variable to store amount of lowercase characters
uppercase = 0 #variable to store amount of uppercase characters
for i in userInput: #for loop that iterates through user input
    if i.islower(): #if statement that checks if the character is lowercase
        lowercase += 1 #if the character is lowercase add 1 to lowercase variable
    else:
        uppercase += 1 #if the character is not lowercase add 1 to uppercase variable
print("No. of upper-case characters: ", str(uppercase)) #print amount of upper-case characters
print("No. of lower-case characters: ", str(lowercase)) #print amount of lower-case characters
