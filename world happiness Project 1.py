#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv('worldhapiness.csv')
print(df)


# In[6]:


# Highlighting the maximum values of each attribute of the data set.
def highlight_max(s):
    is_max = s == s.max()
    return['background-color: limegreen' if v else ''for v in is_max]
df.style.apply(highlight_max)


# In[7]:


# checking the shape of data set
df.shape


# In[8]:


# Plotting the pairwise relationship in the data set
sns.pairplot(df)


# In[20]:


# High, mid , low according to there Happiness.
print('max:',df['Happiness Score'].max())
print('min:',df['Happiness Score'].min())
add=df['Happiness Score'].max()-df['Happiness Score'].min()
grp=round(add/3,3)
print('range difference:',(grp))


# In[21]:


low=df['Happiness Score'].min()+grp
mid=low+grp

print('upper bound of Low grp',low)
print('upper bound of Mid grp',mid)
print('upper bound of High grp','max:',df['Happiness Score'].max())


# In[22]:


df.info()


# In[34]:


fig, axes = plt.subplots(nrows=2, ncols=2,constrained_layout=True,figsize=(12,8))

sns.barplot(x='Economy (GDP per Capita)',y='Country',data=df.nlargest(10,'Economy (GDP per Capita)'),ax=axes[0,0],palette="Blues_d")
sns.barplot(x='Family' ,y='Country',data=df.nlargest(10,'Family'),ax=axes[0,1],palette="YlGn")
sns.barplot(x='Health (Life Expectancy)' ,y='Country',data=df.nlargest(10,'Health (Life Expectancy)'),ax=axes[1,0],palette='OrRd')
sns.barplot(x='Freedom' ,y='Country',data=df.nlargest(10,'Freedom'),ax=axes[1,1],palette='YlOrBr')


# In[31]:


fig, axes = plt.subplots(nrows=1, ncols=2,constrained_layout=True,figsize=(10,4))

sns.barplot(x='Generosity' ,y='Country',data=df.nlargest(10,'Generosity'),ax=axes[0],palette='Spectral')
sns.barplot(x='Dystopia Residual' ,y='Country',data=df.nlargest(10,'Dystopia Residual'),ax=axes[1],palette='RdYlGn')


# In[37]:


df.loc[df['Country']=='India']


# In[38]:


#comparison for the some random countries to check insights
data={
    'Country':['Switzerland','Iceland','Denmark','Norway'],
    'Score':[7.587,7.561,7.527,7.522],
    'Economy (GDP per Capita)':[1.39651,1.30232,1.32548,1.459],
    'Family':[1.34951,1.40223,1.36058,1.33095],
    'Health (Life Expectancy)':[0.94143,0.94784,0.87464,0.88521],
    'Freedom':[0.66557,0.62877,0.64938,0.66973],
    'Generosity':[0.29678,0.4363,0.34139,0.34699],
    'Dystopia Residual':[2.51738,2.70201,2.49204,2.46531]}

d=pd.DataFrame(data)
d


# In[39]:


#Family vs GDP per capita vs Healthy life expectancy

ax = d.plot(y="Family", x="Country", kind="bar",color='C3')
d.plot(y="Economy (GDP per Capita)", x="Country", kind="bar", ax=ax, color="C1")
d.plot(y="Health (Life Expectancy)", x="Country", kind="bar", ax=ax, color="C2")

plt.show()


# In[ ]:




