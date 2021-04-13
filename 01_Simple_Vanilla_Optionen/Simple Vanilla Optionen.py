#!/usr/bin/env python
# coding: utf-8

#Long Call

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline

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



#Short Call

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline


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



#Long Put

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline

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



#Short Put

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline

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
