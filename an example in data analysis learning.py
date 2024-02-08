#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


df = pd.read_csv ('/Users/macos2020/Documents/sample/FSIDOWNLOAD.csv')


# In[22]:


get_ipython().system('head data/Users/macos2020/Documents/sample/FSIDOWNLOAD.csv')


# In[20]:


dataset = pd.read_csv ('/Users/macos2020/Documents/sample/FSIDOWNLOAD.csv')
dataset.head(10)


# In[24]:


dataset.shape


# In[25]:


dataset.info


# In[27]:


dataset['Total'].describe()


# In[32]:


dataset['Total'].plot(kind='box', vert=False, figsize=(14,6))


# In[33]:


dataset['Total'].plot(kind='density', figsize=(14,6)) # kde


# In[35]:


ax = dataset['Total'].plot(kind='density', figsize=(14,6)) # kde
ax.axvline (dataset['Total'].mean(),color='red')
ax.axvline (dataset['Total'].median(),color='green')


# In[34]:


ax = dataset['Total'].plot(kind='hist', figsize=(14,6)) # kde
ax.set_ylabel('Economy')
ax.set_xlabel('Human Rights')


# In[38]:


dataset = pd.read_csv ('/Users/macos2020/Documents/sample/Orders.csv')
dataset.head(20)


# In[48]:


dataset['Product Category'].value_counts()


# In[49]:


dataset['Product Category'].value_counts().plot(kind='pie', figsize=(6,6))


# In[50]:


ax=dataset['Product Category'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Profit')


# In[55]:


corr = dataset.corr()

corr


# In[56]:


fig=plt.figure(figsize=(8,8))
plt.matshow(corr,cmap='RdBu',fignum=fig.number)
plt.xticks(range(len(corr.columns)),corr.columns,rotation='vertical');
plt.yticks(range(len(corr.columns)),corr.columns);


# In[ ]:


dataset.plot(kind='scatter',x='Product Category',y='Profit',figsize=(6,6))


# In[57]:


dataset.plot(kind='scatter',x='Profit',y='Unit Price',figsize=(6,6))


# In[ ]:





# In[ ]:




