#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# Generate variables
# * trust and certinity ranges [0, 1]
# * confidnce range [0, 2]

agent_confidnce = np.arange(0, 2, 1)
agent_Trust = np.arange(0, 1, 1)
agent_Trust_Importance = np.arange(0, 1, 1)
agent_Certainty = np.arange(0, 1, 1)

# Generate fuzzy membership functions

High_Trust_Importance = fuzz.trimf(agent_Trust_Importance, [1, 1, 1])
low_Trust_Importance = fuzz.trimf(agent_Trust_Importance, [0.25, 0.5, 0.5])
High_Trust = fuzz.trimf(agent_Trust, [0.7, 1, 1])
Low_Trust = fuzz.trimf(agent_Trust, [0, 0.4, 0.5])
Average_Trust = fuzz.trimf(agent_Trust, [0.5, 0.7, 0.7])
No_Trust  = fuzz.trimf(agent_Trust, [0, 0, 0])
Low_Certainty = fuzz.trimf(agent_Certainty, [0, 0.4, 1])
High_Certainty = fuzz.trimf(agent_Certainty, [0.7, 1, 1])
Low_confidnce = fuzz.trimf(agent_confidnce, [0, 0.5, 0.5])
High_confidnce = fuzz.trimf(agent_confidnce, [1.25, 2, 2])
Low_confidnce = fuzz.trimf(agent_confidnce, [0, 0.9, 0.9])


# In[57]:


cer = input("Enter certinity value: ")
cer = float(cer)
tru = input("Enter trust value: ")
tru = float(tru)


# In[58]:



if cer > 0.5 and tru > 0.5:
    print ('hight confidence ')
    
if cer > 0.5 and tru > 0.5:
    print ('medium confidence')
       
if cer > 0.5 and tru < 0.5:
    print ('average confidence ')
    
if cer <= 0.5 and tru >= 0.5:
     print ('hight confidence ')
        
if cer <= 0.5 and tru <= 0.5:
    print ('average confidence')
if cer <= 0.5 and tru <= 0.5:
    print ('low confidence low')
    



# In[ ]:




