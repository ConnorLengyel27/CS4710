import matplotlib.pyplot

ProgrammingLanguages = "Java", "Python", "PHP", "JavaScript", "C#", "C++"
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

fig, ax = matplotlib.subplots()
ax.pie(Popularity, labels=ProgrammingLanguages, autopct='%1.1f%%')
