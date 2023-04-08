import pandas as pd
import matplotlib

df = pd.read_csv("data.csv") #import data from data.csv as dataframe

print(pd.DataFrame.describe(df)) #Shows basic statistical description of data
df.fillna(df.mean()) #finds and replaces null values with mean

df.agg({"Duration" : ['min', 'max', 'count', 'mean'], "Calories" : ['min', 'max', 'count', 'mean']}) #Aggregates two columns by min, max, count, and mean
print(df[df['Calories'].between(500,1000)]) #Filters rows with calories value greater than 500 and less than 1000
print(df[(df['Calories'] > 500) & (df['Pulse'] < 100)]) #Filters rows with calories value greater than 500 and pulse value less than 100
df_modified = df.drop("Maxpulse", axis=1) #Creates new df_modified dataframe and deletes maxpulse column
df = df.drop("Maxpulse", axis=1) #Deletes maxpulse column from main dataframe
df["Calories"] = pd.to_numeric(df["Calories"]) #Coverts calories column to ints
scatterplot = df.plot.scatter(x="Duration", y="Calories") #Creates scatterplot with Duration being the x axis and Calories being the y axis
matplotlib.pyplot.show() #Displays the scatterplot
