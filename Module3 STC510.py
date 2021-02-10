#!/usr/bin/env python
# coding: utf-8

# In[11]:


#panda's is the name of the game
import pandas as pd
#added low_memory to fix and error, unsure what it means
n = pd.read_csv('crimestat.csv', low_memory=False)


# In[10]:


n
#occurred to has a missing data


# In[13]:


#looking to see what kind of crimes happen where
n.sort_values(by=['ZIP','UCR CRIME CATEGORY'],ascending=[True,True])


# In[25]:


#this makes UCR CRIME C its own dataframe
ncrimes = n.groupby(['UCR CRIME CATEGORY'])


# In[24]:


#a cleaner version of the above code. Just the crime and ZIP without extra info
ncrimes.ZIP.value_counts()


# In[ ]:


#I need to look how to sort using ncrimes and another header that has spaces, I tried doing something like npub.PREMISE TYPE.value_counts
#but the space is throwing me off, need to look into that


# In[ ]:





# In[ ]:




