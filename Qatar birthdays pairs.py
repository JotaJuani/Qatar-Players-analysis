#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np 
import math
from itertools import combinations


# In[25]:


df = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\data\qatar_players_analysis\qatar_2022_players_data.csv")


# In[26]:


df


# In[27]:


df.columns


# In[28]:


## implement the birthday probability function
def nCr (n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n - k))
    


# In[29]:


#count players per team 
df['nacionalidad'].value_counts()


# In[30]:


# % possibility of players being born the same day
1 - ((364 / 365) ** nCr(26,2))


# In[31]:


#who were born the same day? 
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])


# In[32]:


#extract the year
df['dia_de_nacimiento'] = df['fecha_nacimiento'].dt.strftime('%m-%d')


# In[33]:


df['dia_de_nacimiento']


# In[50]:


team1_df = df.loc[df['nacionalidad'] == 'South Korea']
team1_df


# In[ ]:





# In[51]:


#wo share from brazil? 
names_df1= pd.DataFrame(combinations(team1_df['nombre_del_jugador'],2), columns=['player 1', 'player 2'])
names_df1


# In[52]:


birthday_comparison =  pd.DataFrame(combinations(team1_df['dia_de_nacimiento'],2), columns=['cumpleaños_1', 'cumpleaños_2'])
birthday_comparison 


# In[53]:


checking_df = pd.concat([names_df1, birthday_comparison], axis=1)
checking_df


# In[54]:


##finally finding the result!
(checking_df['cumpleaños_1'] == checking_df[ 'cumpleaños_2']).sum()


# In[55]:


checking_df[(checking_df['cumpleaños_1'] == checking_df[ 'cumpleaños_2'])]


# In[ ]:




