import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic= pd.read_csv("train.csv")
cols= ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"] #selecting columns
titanic= titanic[cols].dropna() #reducing into chosen columns and dropping rows that don't have values 

### Seaborn!!!!!###

# histogram
sns.distplot(titanic["Age"])

# kernel density
sns.set_style('white') #Need to have this first, default is darkgrid. Types: darkgrid, whitegrid, dark, white, ticks
sns.kdeplot(titanic["Age"], shade= True)
sns.despine(left=True, bottom=True) #Removing Spine(boundary)
plt.xlabel("Age")

### Seaborn - **FacetGrid** (this is pretty nice)
## 각 클라스마다 연령대 분포 

#1 creates separate plot for each unique value (1, 2, 3 *일반석, 비즈니스석, 퍼스트클래스 뭐 이렇겟지 ) 
t = sns.FacetGrid(titanic, col= "Pclass", size =6)

#2 each plot to have kernel density plot of "Age" column 
t.map(sns.kdeplot, "Age", shade= True)

#3 just design
t.despine(left= "True", bottom= "True")
plt.show() 

