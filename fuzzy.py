#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# Generate universe variables
# * Quality and service on subjective ranges [0, 1]
# * Tip has a range of [0, 25] in units of percentage points
agent_confidnce = np.arange(0, 1, 1)
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


# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(agent_Trust, Low_Trust, 'b', linewidth=1.5, label='low Trust')
ax0.plot(agent_Trust, Average_Trust, 'g', linewidth=1.5, label='average Trust')
ax0.plot(agent_Trust, High_Trust, 'r', linewidth=1.5, label='high Trust')
ax0.set_title('Agent Confidnce')
ax0.legend()

ax1.plot(agent_Certainty, Low_Certainty, 'b', linewidth=1.5, label='no certinity')
ax1.plot(agent_Certainty, 'g', linewidth=1.5, label='Certain')
ax1.set_title('agent_Certainty')
ax1.legend()

ax2.plot(x_tip, tip_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_tip, tip_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_tip, tip_hi, 'r', linewidth=1.5, label='High')
#ax2.set_title('Tip amount')
#ax2.legend()




# In[ ]:




