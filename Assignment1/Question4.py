it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} #creates it_companies set
A = {19, 22, 24, 20, 25, 26} #creates A set
B = {19, 22, 20, 25, 26, 24, 28, 27} #creates B set
age = [22, 19, 24, 25, 26, 24, 25, 24] #creates age list
print(len(it_companies)) #prints length of it_companies est
it_companies.add('Twitter') #adds Twitter to it_companies set
temp = {'Dell', 'HP'} #creates temp set
it_companies.update(temp) #adds temp set to it_companies set
it_companies.remove('Facebook') #removes Facebook from it_companies est
#when discard is used no error is raised when the item is not in the set, however remove raises an error when the item is not in the set
A.update(B) #joins A and B
print(A.intersection(B)) #finds intersection of A and B
print(A.issubset(B)) #finds if A is a subset of B
print(A.isdisjoint(B)) #finds if A and B are disjoint sets
A.update(B) #joins A with B
B.update(A) #joins B with A
print(A.symmetric_difference(B)) #prints symmetric difference of A and B
A = {} #removes all elements of A
B = {} #removes all elements of B
ages = set(age) #creates ages set with age list
print("The length of the ages set is " + str(len(ages)) + " and the length of the ages list is " + str(len(age))) #compares length of ages set and age list
