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
g = sns.FacetGrid(titanic, col= "Pclass", size =6)

#2 each plot to have kernel density plot of "Age" column 
g.map(sns.kdeplot, "Age", shade= True)


## 조건 더 추가할 수 있음!!!!!!!!!!

# survived yes or no -> Class 1,2,3 -> 연령대 분포! [6 plots]
g = sns.FacetGrid(titanic, col="Survived", row="Pclass") 
g.map(sns.kdeplot, "Age", shade=True) 

# survived men, survived women, dead men, dead women 연령대 분포! [4 plots]
g = sns.FacetGrid(titanic, col="Survived", row="Sex")
g.map(sns.kdeplot, "Age", shade=True)


# 3가지 조건을 달고 연령대 분포 보기 @@@@ IMPORTANT @@@@
# survived yes or no -> class 1, 2, 3 -> Age distribution per sex in different colors!!
# So, total of 6 charts, and each chart has two plots of men and women distrubition of age 
g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue= "Sex", size=3) 
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend() #Legend가 있어야지 어느색이 남자 여자인지를 알 수 있겠지?
sns.despine(left=True, bottom=True)
plt.show()

