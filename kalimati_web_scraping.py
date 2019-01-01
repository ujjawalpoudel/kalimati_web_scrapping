#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import requests
import pandas as pd

# api-endpoint
URL = "http://kalimatimarket.gov.np/priceinfo/dlypricebulletin" # URL that hit API to get data as post method

date = "12/01/2018" # for manula input date

#pricetype
pricetype = "W"    # W for  थोक   and R for खुद्रा

# defining a params dict for the parameters to be sent to the API
PARAMS = {'cdate':date,'pricetype':pricetype}

# sending post request and saving the response as response object
r = requests.post(url=URL,data=PARAMS)

# response is convert in string
rtext = r.text

# string is converted in list , it exatract html table into dataframe
list_convert = (pd.read_html(io = rtext))[1]

# list is converted into dataframe
df = pd.DataFrame(list_convert)

df = df[2:]
df.columns = df.iloc[0]
df=df[1:]

month = 12         # Enter month for manual input of date
year = 2018
df = df.assign(date = date )
df = df.assign(month = month )
df = df.assign(year = year )

cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

df.to_csv("kalimati_scrapping.csv", index=False)


# In[ ]:




