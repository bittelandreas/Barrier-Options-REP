#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import numpy as np  
import pandas as pd  
import pandas_datareader as wb  
import matplotlib.pyplot as plt
import time
from math import log, sqrt, pi, exp
from pandas import DataFrame
from scipy.stats import norm
from datetime import datetime, date
get_ipython().run_line_magic('matplotlib', 'inline')


#Settings for Monte Carlo asset data, how long, and how many forecasts 

today = date.today()

cp = input("Willst du einen Call (c) oder einen Put (p) berechnen?");
ticker = input("YahooFinance-Ticker: ") #NVS'
expiry = time(input("Verfall (mm-dd-yyyy): ")#'04-16-2021'
diff = expiry-today
t_intervals = diff.days # time steps forecasted into future
iterations = input("Anzahl Simulationen: ") # amount of simulations


#Acquiring data

data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start= today)['Adj Close']

#Preparing log returns from data
log_returns = np.log(1 + data.pct_change())


# In[7]:


#Setting up drift and random component in relation to asset data

u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
#Takes last data point as startpoint point for simulation
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0
#Applies Monte Carlo simulation in asset
for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

#Plot simulations
plt.figure(figsize=(10,6))
plt.plot(price_list);


# In[ ]:


def d1(S,K,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)


# In[ ]:


def bs_call(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
def bs_put(S,K,T,r,sigma):
    return K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))-S*norm.cdf(-d1(S,K,T,r,sigma))


# In[ ]:



df = wb.DataReader(ticker, data_source='yahoo', start='2018-1-1')
df = df.sort_values(by="Date")
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)

S = price_list[-1].mean()
strike_price = float(input("Strike: "))
sigma = np.sqrt(252) * df['returns'].std()
r = -0.0028
t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365

if (cp == "c"):
    print('The Option Price is: ', round(bs_call(S, strike_price, t, r, sigma),2))
else:
    print('The Option Price is: ', round(bs_put(S, strike_price, t, r, sigma),2))

