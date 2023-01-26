dog = {} #creates empty dictionary titled dog
dog.update({"name": ""}) #adds name to dog dictionary
dog.update({"color": ""}) #adds color to dog dictionary
dog.update({"breed": ""}) #adds breed to dog dictionary
dog.update({"legs": ""}) #adds legs to dog dictionary
dog.update({"age": ""}) #adds age to dog dictionary
student = {"first_name": "", "last_name": "", "gender": "", "age": "", "marital_status": "", "skills": ["skill1", "skill2"], "country": "", "city": "", "address": ""} #creates student dictionary
print(len(student)) #prints length of student dictionary
print(student.get("skills")) #prints student dictionary skills
print(type(student.get("skills"))) #prints data type of student dictionary skills
student["skills"] += ["skill3"] #adds 3rd skill to student dictionary skills
print(student.get("skills")) #prints student dictionary skills
print(student.keys()) #prints student dictionary keys as list
print(student.values()) #prints student dictionary values as list
