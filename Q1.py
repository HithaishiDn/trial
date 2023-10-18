#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


customers = pd.read_csv('customers.csv')
transactions = pd.read_csv('transactions.csv')
orders = pd.read_csv('orders.csv')


# In[21]:


data = pd.merge(transactions, orders, on='order_id')
data = pd.merge(data, customers, on='customer_id')


# In[22]:


data.shape


# In[23]:


data.columns


# In[24]:


data.isnull().sum()


# In[25]:


#high-value transactions (sales amount >150)
high_value =data[(data['sales'] > 150)]
high_value
 


# In[26]:


#list of orders id having high-value transactions (sales amount >150)
final=high_value[['order_id','sales']]
final


# In[27]:


#list of customers who placed orders having high-value transactions
final=high_value[['customer_id','customer_name','sales']]
final


# In[ ]:





# In[ ]:




