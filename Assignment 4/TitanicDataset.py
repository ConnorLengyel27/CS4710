import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv") #import data from train.csv as dataframe

corr = df.Sex.str.get_dummies(sep=' ').corrwith(df.Survived/df.Survived.max()) #determines correlation between survived and sex
print(corr)

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4)) #sets fig and axes variables
women = df[df['Sex']=='female'] #sets women variable to data in women column
men = df[df['Sex']=='male'] #sets men variable to data in men column
ax = sns.histplot(women[women['Survived']==1].Age.dropna(), bins=18, label = 'survived', ax = axes[0], kde =False) #plots women survived graph
ax = sns.histplot(women[women['Survived']==0].Age.dropna(), bins=40, label = 'not survived', ax = axes[0], kde =False) #plots women not survived graph
ax.legend() #creates legend
ax.set_title('Female') #sets title of graph
ax = sns.histplot(men[men['Survived']==1].Age.dropna(), bins=18, label = 'survived', ax = axes[1], kde = False) #plots men survived graph
ax = sns.histplot(men[men['Survived']==0].Age.dropna(), bins=40, label = 'not survived', ax = axes[1], kde = False) #plots men not survived graph
ax.legend() #creates legend
_ = ax.set_title('Male') #sets title of graph
plt.show() #Displays the visualizations
