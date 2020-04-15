#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split


# In[2]:


from sklearn.datasets import load_boston
boston = load_boston()
print(boston)


# In[3]:


df_x = pd.DataFrame(boston.data, columns = boston.feature_names)
df_y = pd.DataFrame(boston.target)


# In[4]:


df_x.describe()


# In[5]:


x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=42)
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)


# In[6]:


print(reg.coef_)


# In[7]:


y_pred = reg.predict(x_test)
print(y_pred)


# In[8]:


from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))


# In[ ]:




