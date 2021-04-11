#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Bibliotheken importieren
import numpy as np  
import pandas as pd
from pandas import DataFrame
import pandas_datareader as wb  
import matplotlib.pyplot as plt
import time
import math
import datetime
from scipy.stats import norm


%matplotlib inline



#Heutiges Datum definieren
today = date.today()

#Berechnungen für Call oder Put Option
cp = input('Call (c) oder Put (p)? (Standardeinstellung: Call) ')
if cp == '':
    cp = 'c'
else:
    cp = cp

#Ticker definieren
ticker = input('YahooFinance-Ticker (Standardeinstellung: Novartis): ')
if ticker == '':
    ticker = 'NVS'
else:
    ticker = ticker

#Verfalldatum der Option definieren
expiry = input("Verfallsdatum (mm-dd-yyyy) (Standardeinstellung: 04-16-2021): ")
if expiry == '':
    expiry = '04-16-2021'
else:
    expiry = expiry

#Tagesdifferenz Heute bis Verfall
month, day, year = map(int, expiry.split('-'))
expiry = datetime.date(year, month, day)
delta = (expiry - today)
time_int = delta.days

#Anzahl Simulationen
iterations = input("Anzahl Simulationen (Standardeinstellung: 10'000): ")
if iterations == '':
    iterations = 10000
else:
    iterations = iterations


#Daten ziehen
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = today)['Adj Close']

#Preparing log returns from data
log_returns = np.log(1 + data.pct_change())


# In[7]:


#Setting up drift and random component in relation to asset data

u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(time_int, iterations)))
#Takes last data point as startpoint point for simulation
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0
#Applies Monte Carlo simulation in asset
for t in range(1, time_int):
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

