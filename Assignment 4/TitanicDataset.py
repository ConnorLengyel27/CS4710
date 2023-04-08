import pandas as pd
import matplotlib

df = pd.read_csv("train.csv") #import data from train.csv as dataframe

corr = df.Sex.str.get_dummies(sep=' ').corrwith(df.Survived/df.Survived.max())
print(corr)
