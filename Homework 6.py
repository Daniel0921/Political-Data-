#!/usr/bin/env python
# coding: utf-8

# In[240]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[241]:


donations = pd.read_csv("C:\\Users\\Danny\\Desktop\\NH_Contribution_v2.csv")


# In[242]:


donations.head()


# In[275]:


donations_new = donations.rename(columns={"contb_receipt_amt":"Contribution_Amount", "contbr_city":"Contribution_City"})
donations_new['Contribution_City'].value_counts()[:5]


# In[278]:


donations_new['cand_nm'].value_counts()[:5]


# In[277]:


donations_new.query('Contribution_City == "PORTSMOUTH" & cand_nm == "Trump, Donald J."', inplace = True)


# In[273]:


sns.boxplot(donations_new['Contribution_Amount'], orient='h')


# In[281]:


donations_new["Contribution_Amount"].mean()

