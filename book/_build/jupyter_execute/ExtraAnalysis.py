#!/usr/bin/env python
# coding: utf-8

# # Extra analysis (do not put in book!)

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv("CollegeRankingsData.csv")
data.head()


# In[3]:


data.MathSAT * data.VerbalSAT


# This is some preliminary analysis that isn't yet ready to be released.
