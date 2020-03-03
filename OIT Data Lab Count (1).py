#!/usr/bin/env python
# coding: utf-8

# # OIT DATA LAB COUNT 

# In[38]:


import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[39]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[40]:


data = pd.read_csv('Lab Sample Data UTF8.csv') #The xlsx file converted to CSV
                                               #Making a data frame for the csv file


# In[41]:


data.head() #Displaying the head


# In[42]:


data['Hill Hall'] #Displaying Hill Hall Lab Counts


# In[76]:


data.drop(data.columns[data.apply(lambda col: col.isnull().sum() > 4)], axis=1, inplace = True) ##Dropping the Columns with NaN values


# In[77]:


data.dropna(thresh = 2, inplace = True) ##Dropping rows with NaN values


# In[62]:





# In[86]:


plt.ion()
data = pd.read_csv('lab Sample Data UTF8.csv')
data.drop(data.columns[data.apply(lambda col: col.isnull().sum() >4)], axis =1, inplace =True)
data.dropna(thresh =2, inplace = True)

data.plot(x = 'Times', y= 'Hill Hall', figsize = (10,5), grid = True)
data.plot(x = 'Times', y = 'RBS',figsize = (10,5), grid = True)
data.plot(x = 'Times', y= 'Englehard', figsize = (10,5), grid = True)
data.plot(x = 'Times', y= 'Cyber Lounge', figsize = (10,5), grid = True)
data.plot(x = 'Times', y= 'Dana', figsize = (10,5), grid = True)
data.plot(x = 'Times', y= 'Englehard', figsize = (10,5), grid = True)
plt.xlabel('Times')
plt.xticks(range(len(data.Times)), data.Times, rotation = 45)
plt.ylabel('Users')
plt.show()


# In[ ]:




