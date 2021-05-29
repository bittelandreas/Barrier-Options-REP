import numpy as np
from math import log, sqrt, pi, exp

def pricing_calldownandout(S, sigma, T, r, J, iterations, L, K):
    
    iterations = int(iterations); J = int(J) ; dt = T/J; t = np.linspace(0,T,J+1)[:,None];
    
    Z = np.random.randn(J,iterations); X = np.cumsum(Z,axis =0)
    
    X = np.vstack((np.zeros(iterations),X));
    
    sJ = S*np.exp((r-0.5*sigma**2)*t+sigma*np.sqrt(dt)*X);
    
    vJ = np.exp(-r*T)*np.mean((np.min(sJ, axis = 0)>L)*np.maximum(sJ[-1]-K, 0))
        
    return vJ                