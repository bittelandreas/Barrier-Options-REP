#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame

#S = 87.55
#K = 92.50
#T = 0.011
#r = -0.0028
#sigma = 0.2001


def d1(S,K,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)


# In[96]:





# In[118]:


d1(S,K,T,r,sigma)


# In[119]:


d2(S,K,T,r,sigma)


# In[2]:


def bs_call(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
def bs_put(S,K,T,r,sigma):
    return K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))-S*norm.cdf(-d1(S,K,T,r,sigma))

#K*exp(-r*T)-S+bs_call(S,K,T,r,sigma)
#K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))-S*norm.cdf(-d1(S,K,T,r,sigma))


# In[13]:


from datetime import datetime, date
import numpy as np
import pandas as pd
import pandas_datareader.data as web

cp = input("Willst du einen Call (c) oder einen Put (p) berechnen?");

stock = input("YahooFinance-Ticker: ")#'NVS'
expiry = input("Verfall (mm-dd-yyyy): ")#'04-16-2021'
strike_price = float(input("Strike: "))#92.50

today = datetime.now()
one_year_ago = today.replace(year=today.year-1)

df = web.DataReader(stock, 'yahoo', one_year_ago, today)

df = df.sort_values(by="Date")
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)

sigma = np.sqrt(252) * df['returns'].std()
uty = -0.0028

#uty = web.DataReader(
    #"^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1]
    
lcp = df['Close'].iloc[-1]
t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365

if (cp == "c"):
    print('The Option Price is: ', round(bs_call(lcp, strike_price, t, uty, sigma),2))
else:
    print('The Option Price is: ', round(bs_put(lcp, strike_price, t, uty, sigma),2))


# In[ ]:




