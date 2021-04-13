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
from datetime import date
from scipy.stats import norm

%matplotlib inline

#Einführung
print('Ihnen werden gleich verschiedene Fragen gestellt, damit Sie die Inputvariablen definieren können.\n'
'Falls Sie dies nicht wünschen, können Sie jeweils mit der "Enter"-Taste durchklicken.\n'
'Folgende Standardeinstellungen würden für die Berechnungen dienen:\n'
'- Option:              Call\n'
'- Ticker:              Novartis\n'
'- Verfallsdatum:       04-16-2021\n'
'- Anzahl Simulationen: 10000')
time.sleep(0.5)

#Heutiges Datum definieren
today = date.today()

#Berechnungen für Call oder Put Option
cp = input('Call (c) oder Put (p)? ')
if cp == '':
    cp = 'c'
else:
    cp = cp
print(cp)

#Ticker definieren
ticker = input('Ticker: ')
if ticker == '':
    ticker = 'NVS'
else:
    ticker = ticker
print(ticker)

#Verfalldatum der Option definieren
expiry = input("Verfallsdatum (mm-dd-yyyy): ")
if expiry == '':
    expiry = '04-16-2021'
else:
    expiry = expiry
print(expiry)

#Tagesdifferenz Heute bis Verfall
month, day, year = map(int, expiry.split('-'))  #Datum wird in Einzelteile zerlegt
expiry = datetime.date(year, month, day)        #Datum wird korrekt formatiert 
delta = (expiry - today)                        #Differenz zwischen heute und Verfallsdatum
time_int = delta.days                           #Differenz wird in Tagen definiert

#Anzahl Simulationen
iterations = input("Anzahl Simulationen: ")
if iterations == '':
    iterations = 10000
else:
    iterations = iterations
print(iterations)


#Daten ziehen
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source = 'yahoo', start = today)['Adj Close']


#Drift vorbereiten und "Zufallsgenerator" erstellen
    #Mit dem Drift wird die .......... definiert

log_returns = np.log(1 + data.pct_change()) #Log returns berechnen
u = log_returns.mean()                      #Mittelwert der log returns
var = log_returns.var()                     #Varianz der log returns
stdev = log_returns.std()                   #Standardabweichung der log returns
drift = u - (0.5 * var)                     #Drift berechnen

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(time_int, iterations)))
#Takes last data point as startpoint point for simulation
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = S0


#Einzelne Monte Carlo Simulation
for t in range(1, time_int):
    price_list[t] = price_list[t - 1] * daily_returns[t]

#Monte Carlo Simulationen werden dargestellt
plt.figure(figsize=(10,6))
plt.plot(price_list);


# In[ ]:

#Black-Scholes berechnen
def bs(S,K,T,r,sigma):
    def d1(S,K,T,r,sigma): #Berechnung von d1
        return(log(S/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))
    def d2(S,K,T,r,sigma): #Berechnung von d2
        return d1(S,K,T,r,sigma)-sigma*sqrt(T)

#Plain Vanilla Optionen berechnen
def bs_call(S,K,T,r,sigma): #Plain Vanilla Call Option
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
def bs_put(S,K,T,r,sigma): #Plain Vanilla Put Option
    return K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))-S*norm.cdf(-d1(S,K,T,r,sigma))


# In[ ]:


df = wb.DataReader(ticker, data_source='yahoo', start='2018-1-1')
df = df.sort_values(by = 'Date')
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)

S = price_list[-1].mean()
K = float(input("Strike: "))
sigma = np.sqrt(252) * df['returns'].std()
r = -0.00283 #Aktueller Zinssatz einer 10y Schweizer Staatsanleihe
t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365

if cp == 'c':
    print('Der Preis für die Call Option beträgt: ', round(bs_call(S, K, t, r, sigma),2))
else:
    print('Der Preis für die Put Option beträgt: ', round(bs_put(S, K, t, r, sigma),2))

