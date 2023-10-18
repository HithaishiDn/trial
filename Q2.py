#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


customers = pd.read_csv('customers.csv')
transactions = pd.read_csv('transactions.csv')
orders = pd.read_csv('orders.csv')


# In[3]:


data = pd.merge(transactions, orders, on='order_id')
data = pd.merge(data, customers, on='customer_id')


# In[5]:


high_value= data[(data['sales'] > 250)]
high_value


# In[7]:


final=high_value[['order_id','sales']]
final


# In[6]:


final=high_value[['customer_id','customer_name','sales']]
final


# In[17]:


high_value['order_delivered_customer_date'] = pd.to_datetime(high_value['order_delivered_customer_date'], errors='coerce', infer_datetime_format=True)
high_value['month_year'] = high_value['order_delivered_customer_date'].dt.to_period("M")


# In[18]:


final = high_value[['order_id', 'customer_id','customer_name', 'sales', 'month_year']]


# In[19]:


final


# In[ ]:





# In[ ]:




