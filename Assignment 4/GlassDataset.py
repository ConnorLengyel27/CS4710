import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


df = pd.read_csv("glass.csv") #Import data from glass.csv as dataframe

nb = GaussianNB() #Creates a Naive Bayes object
x = df.drop(columns=['Type']) #Creates x variable
y = df['Type'] #Creates y variable
x_train, x_true, y_train, y_true = train_test_split(x, y, test_size=0.2, random_state=4) #Split data into training and true data
nb.fit(x_train, y_train) #Trains the model
y_pred = nb.predict(x_true) #Predicts testing set
print(classification_report(y_true, y_pred)) #Prints classification report

svmMod = SVC() #Creates a svm object
svmMod.fit(x_train,y_train) #Sets x_train and y_train
y_pred = svmMod.predict(x_true) #Predicts testing set
print(classification_report(y_true, y_pred)) #Prints classification report
