#!/usr/bin/env python
# coding: utf-8

# ***Exploratory Data Analysis On Titanic Dataset***

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# df=pd.read_csv("C:/Users/Wahab/Downloads/Titanic Data/titanic/train.csv")

# In[174]:


df.shape


# In[175]:


df.head(10)


# In[176]:


print(df.isna().any())


# In[177]:


print(df.isna().sum())


# In[178]:


df.info()


# In[227]:


print(df.duplicated().sum())


# In[180]:


df.drop("Cabin",axis='columns',inplace=True)


# In[181]:


df


# In[182]:


# train['Age'].fillna(train['Age'].mean(),inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())


# In[183]:


df.info()


# In[184]:


df['Embarked'].value_counts()


# In[185]:


df['Embarked']=df['Embarked'].fillna('S')
# type(df['Embarked'])


# In[186]:


df.info()


# In[187]:


df["Parch"].value_counts() 


# In[188]:


df["SibSp"].value_counts() 


# In[189]:


df.info()


# In[190]:


df["Survived"]=df["Survived"].astype('category')
df["Parch"]=df["Parch"].astype('category')
df["Sex"]=df["Sex"].astype('category')
df["Age"]=df["Age"].astype('int')
df["SibSp"]=df["SibSp"].astype('category')
df["Embarked"]=df["Embarked"].astype('category')


# In[191]:


df.info()


# In[192]:


df.describe()


# In[202]:


sns.countplot(data=df,x='Survived')
plt.title("Survival Count")


# In[203]:


death_percent=round((df['Survived'].value_counts().values[0]/891)*100)


# In[204]:


print("out of 891, {}%  people died in the accident".format(death_percent))


# In[205]:


print(round((df['Pclass'].value_counts()/891)*100))


# In[208]:


sns.countplot(data=df,x='Pclass',hue='Survived')
plt.title('Survival Count Based on Passenger Class')


# In[198]:


# class_survived=df[df['Survived']==1]


# In[209]:


sns.countplot(data=df,x='Sex',hue='Survived')
plt.title('Survival Count Based on Gender')


# In[157]:


sns.countplot(data=df,x='SibSp')


# In[210]:


sns.countplot(data=df,x='SibSp',hue='Survived')
plt.title('Survival Count Based on Sibling/Spouse')


# In[201]:


df['Fare'].hist(bins=50)
plt.title('Distribution of Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()


# In[211]:


print("Skewness of Fare column is",df['Fare'].skew())
print("Kurtosis of Fare column is",df['Fare'].kurt())


# In[160]:


print("People with Fare between 200$ and 300$ are", df[(df['Fare']>200) & (df['Fare']<300)].shape[0] )


# In[161]:


print("People with Fare greater than 300$ are", df[(df['Fare']>300)].shape[0] )


# In[110]:


sns.pairplot(df)


# In[212]:


df['Parch']=df['Parch'].astype('int')
df['SibSp']=df['SibSp'].astype('int')


# In[213]:


df['Family']=df['Parch']+df['SibSp']


# In[214]:


df.sample(10)


# In[165]:


df.drop(['Parch','SibSp'],axis='columns',inplace=True)


# In[166]:


df.sample(10)


# In[215]:


sns.countplot(data=df,x="Embarked",hue='Survived')
print("Percentage of people embarked from each city",(df['Embarked'].value_counts()/891)*100)
print("Percentage of people survived from each city",(class_survived['Embarked'].value_counts()/891)*100)


# In[225]:


sns.histplot(data=df,x='Age',hue='Survived')


# In[226]:


sns.catplot(data=df, x='Embarked', hue='Pclass', col='Survived', kind='count')


# In[228]:


sns.histplot(data=df, x='Age', hue='Survived', multiple='stack')
plt.title('Age Distribution by Survival Status')


# In[ ]:




