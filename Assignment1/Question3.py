brothers = ("John", "Joel", "Bob") #creates brothers tuple
sisters = ("Sarah", "Jill", "Claire") #creates sisters tuple
siblings = brothers + sisters #joins brothers and sisters tuples
print(len(siblings)) #prints amount of siblings
temp = ("Leon", "Nora") #temp tuple containing parents names
siblings += temp #adds father and mother to siblings tuple
family_members = siblings #assigns values of siblings tuple to family_members tuple
print(family_members) #prints family_members tuple
