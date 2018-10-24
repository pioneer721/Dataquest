import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic= pd.read_csv("train.csv")
cols= ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"] #selecting columns
titanic= titanic[cols].dropna() #reducing into chosen columns and dropping rows that don't have values 

###Seaborn!!!!!

# histogram
sns.distplot(titanic["Age"])

# kernel density
sns.kdeplot(titanic["Age"], shade= True)
plt.xlabel("Age")
