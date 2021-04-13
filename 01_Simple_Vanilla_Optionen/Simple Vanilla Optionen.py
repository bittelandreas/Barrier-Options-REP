#!/usr/bin/env python
# coding: utf-8

# Hilpisch, 2015, S. 9f.

# In[119]:


#
# European Call Option Inner Value Plot
# 02_MBV/inner_value_plot.py
#
# (c) Dr. Yves J. Hilpisch
# Derivatives Analytics with Python
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Option Strike
K = 8000
# Graphical Output
S = np.linspace(7000, 9000, 100) # index level values
h = np.maximum(S - K, 0) # inner values of call option
plt.figure()
plt.plot(S, h, lw=2.5) # plot inner values at maturity
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of European call option')
plt.grid(True)


# Angepasst:

# In[140]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Strike Preis
K = 100
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.maximum(S - K, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True)
ax.set_ylim(bottom = 20)
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[159]:


#Long Call

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'qt')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.maximum(S - K, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -1, 1, linestyles ="dashed", colors ="r")
plt.vlines(110, -1, 1, linestyles ="dashed", colors ="g")
plt.vlines(115, -1, 5.5, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Long Call')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[158]:


#Long Call

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.maximum(S - K, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -1, 1, linestyles ="dashed", colors ="r")
plt.vlines(110, -1, 1, linestyles ="dashed", colors ="g")
plt.vlines(115, -1, 5.5, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Long Call')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[160]:


#Short Call

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'qt')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.minimum(K - S, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -10, 0.6, linestyles ="dashed", colors ="r")
plt.vlines(110, -10, 0.6, linestyles ="dashed", colors ="g")
plt.vlines(115, -10, -4.5, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Short Call')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[154]:


#Short Call

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.minimum(K - S, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -10, 0.6, linestyles ="dashed", colors ="r")
plt.vlines(110, -10, 0.6, linestyles ="dashed", colors ="g")
plt.vlines(115, -10, -4.5, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Short Call')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[168]:


#Long Put

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.maximum(K - S, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -1, 10.5, linestyles ="dashed", colors ="r")
plt.vlines(110, -1, 1, linestyles ="dashed", colors ="g")
plt.vlines(115, -1, 1, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Long Put')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[169]:


#Long Put

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'qt')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.maximum(K - S, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -1, 10.5, linestyles ="dashed", colors ="r")
plt.vlines(110, -1, 1, linestyles ="dashed", colors ="g")
plt.vlines(115, -1, 1, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Long Put')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[172]:


#Short Put

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.minimum(S - K, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -10.5, 1, linestyles ="dashed", colors ="r")
plt.vlines(110, -1, 1, linestyles ="dashed", colors ="g")
plt.vlines(115, -1, 1, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Short Put')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[173]:


#Short Put

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'qt')

# Strike Preis
K = 110
# Marktpreis
S = np.linspace(95, 120)
# Payoff
h = np.minimum(S - K, 0)

# Grafik
plt.figure()
plt.plot(S, h, lw = 2)
plt.grid(True, alpha = 0.3)
plt.vlines(100, -10.5, 1, linestyles ="dashed", colors ="r")
plt.vlines(110, -1, 1, linestyles ="dashed", colors ="g")
plt.vlines(115, -1, 1, linestyles ="dashed", colors ="r")

plt.title('Payoff Diagramm Short Put')
plt.xlabel('Marktpreis $S$ zum Zeitpunkz T bzw. T+1')
plt.ylabel('Payoff')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# https://blog.quantinsti.com/long-strangle-option-strategy-in-python/

# In[34]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn

# Fortis stock price 
spot_price = 138.90

# Long put
strike_price_long_put = 135
premium_long_put = 4

# Long call
strike_price_long_call = 145 
premium_long_call = 3.50

# Stock price range at expiration of the put
sT = np.arange(0.7*spot_price,1.3*spot_price,1)

def call_payoff(sT, strike_price, premium):
       return np.where(sT > strike_price, sT - strike_price, 0) - premium
payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)

# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call,label='Long Call',color='r')
plt.xlabel('Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()


# Angepasst

# In[61]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn

get_ipython().run_line_magic('matplotlib', 'qt')

# Fortis stock price 
spot_price = 98

# Strike Preis
K = 100 
Premium = 1.20

# Stock price range at expiration of the call
sT = 125

def call_payoff(sT, K, Premium):
       return (np.where(sT > K, sT - K, 0) - Premium)

#Payoff   
payoff = call_payoff(sT, K, Premium)

# Plot
fig, ax = plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT, payoff, label='Long Call',color='r')
plt.xlabel('Marktpreis $s_T$')
plt.ylabel('Payoff')
plt.grid(True)
plt.legend()
plt.show()


# In[65]:


call_payoff(sT, K)


# In[63]:


def call_payoff(sT, K):
       return np.where(sT > K, sT - K, 0)


# In[75]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Strike Preis
K = 100
# Marktpreis
S = np.linspace(90, 130, num = 5)

# Stock price range at expiration of the call
sT = 125

Premium = 1.20
# Payoff
def call_payoff(sT, K, Premium):
       return (np.where(sT > K, sT - K, 0) - Premium)

#Payoff
payoff = call_payoff(sT, K, Premium)

# Grafik
plt.figure()
plt.plot(98, call_payoff(sT, K, Premium), lw = 2)
plt.grid(True)
plt.xlabel('Marktpreis $S_t$ at maturity')
plt.ylabel('Payoff')


# In[81]:


pip install opstrat


# In[85]:


import opstrat as op

get_ipython().run_line_magic('matplotlib', 'inline')

op.single_plotter()


# In[86]:


op.single_plotter(spot=460, strike=460, op_type='p', tr_type='s', op_pr=12.5)


# In[96]:


import opstrat as op

#Parameters

#op_type: kind {'c','p'}, default:'c'
 # Opion type>> 'c': call option, 'p':put option

#spot: int, float, default: 100
 #Spot Price

#spot_range: int, float, optional, default: 5
 #Range of spot variation in percentage

#strike: int, float, default: 102
 #Strike Price

#tr_type: kind {'b', 's'} default:'b'
 #Transaction Type>> 'b': long, 's': short

#op_pr: int, float, default: 10
 #Option Price


op.single_plotter(spot=98, strike = 100, op_type='c', tr_type='b', op_pr = 1.2)


# https://github.com/abhijith-git/opstrat/blob/main/README.md

# In[117]:


get_ipython().run_line_magic('matplotlib', 'qt')

op.single_plotter(spot=100, strike = 110, op_type='c', tr_type='b', op_pr = 0)


# In[116]:


op.single_plotter(spot=80, strike = 100, op_type='c', tr_type='b', op_pr = 1)


# In[118]:


get_ipython().run_line_magic('matplotlib', 'qt')

op.single_plotter(spot=100, strike = 110, op_type='c', tr_type='b', op_pr = 0)


# In[ ]:




