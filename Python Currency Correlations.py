#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os                      
import requests, io            
import zipfile as zf            
import shutil       


# In[2]:


url = "/Users/jameshu/Downloads/currency_exchange_rate.csv"
currencies = pd.read_csv(url)
currencies


# In[3]:


currencies = currencies.drop(currencies.columns[[0]], axis=1)


# In[4]:


print(currencies['LOCATION'].unique())


# In[5]:


values = list(range(1950,2000))
values2 = list(range(2015,2021))
currencies = currencies[currencies.TIME.isin(values) == False ]
currencies


# In[6]:


top10 = ('USA','EU28','JPN','GBR','AUS','CAN','SWE','CHN','HKG','NZL')
topcurrencies = currencies[currencies.LOCATION.isin(top10) == True]
topcurrencies


# In[7]:


topcurrencies.set_index('TIME', inplace=True)
topcurrencies.groupby('LOCATION')['Value'].plot(legend=True)


# In[8]:


topcurloc = topcurrencies['LOCATION']
topcurval = topcurrencies['Value']
newcurr = pd.concat([topcurloc,topcurval], axis=1).reset_index()
newcurr


# In[12]:


AUScur = newcurr['LOCATION'] == 'AUS'
AUSc = newcurr.loc[AUScur,:]
EUcur = newcurr['LOCATION'] == 'EU28'
EUc = newcurr.loc[EUcur,:]
EUc = EUc.reset_index()
JPNcur = newcurr['LOCATION'] == 'JPN'
JPNc= newcurr.loc[JPNcur,:]
JPNc = JPNc.reset_index()
GBRcur= newcurr['LOCATION'] == 'GBR'
GBRc = newcurr.loc[GBRcur,:]
GBRc = GBRc.reset_index()
CHNcur = newcurr['LOCATION'] == 'CHN'
CHNc = newcurr.loc[CHNcur,:]
CHNc = CHNc.reset_index()
HKGcur = newcurr['LOCATION'] == 'HKG'
HKGc = newcurr.loc[HKGcur,:]
HKGc = HKGc.reset_index()
NZLcur = newcurr['LOCATION'] == 'NZL'
NZLc = newcurr.loc[NZLcur,:]
NZLc = NZLc.reset_index()
CANcur = newcurr['LOCATION'] == 'CAN'
CANc = newcurr.loc[CANcur,:]
CANc = CANc.reset_index()
SWEcur = newcurr['LOCATION'] == 'SWE'
SWEc = newcurr.loc[SWEcur,:]
SWEc = SWEc.reset_index()


# In[13]:


currdict = {'AUS':AUSc['Value'],'GBR':GBRc['Value'],'NZL':NZLc['Value'],'EU28':EUc['Value'],'HKG':HKGc['Value'],'CHN':CHNc['Value'],'SWE':SWEc['Value'],'CAN':CANc['Value'],'JPN':JPNc['Value']}
currency_location = pd.DataFrame.from_dict(currdict)
currency_location


# In[15]:


correlation_data = currency_location.corr()
correlation_data


# In[16]:


c = correlation_data.abs()
s = c.unstack()
so = s.sort_values(kind="quicksort")
correlation_graph = so.iloc[0:72].iloc[::2]
correlation_graph.plot(kind = 'barh',figsize = (20,10))


# In[17]:


correlation_data.style.background_gradient(cmap="Blues")


# In[18]:


correlation_graph


# In[ ]:




