
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime


# In[2]:


#these are the stocks we can choose in our portfolio
stocks = ['AAPL']

#we use historical data to approximate mean and variance: MPT depends on historical data !!!
start_date='01/01/2010'
end_date ='01/01/2017'

#downloading the data from Yahoo! Finance
def download_data(stocks):
	data = web.DataReader(stocks,data_source='yahoo',start=start_date,end=end_date)['Adj Close']	
	return data


# In[5]:


a = download_data(stocks)[:10]


# In[6]:


def calc_return (data):
    r = np.log(data-data.shift(1)/data.shift(1))
    return r

calc_return()

