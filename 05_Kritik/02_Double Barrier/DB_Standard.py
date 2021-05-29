import numpy as np
from math import log, sqrt, pi, exp

def pricing_cudo(S, sigma, T, r, J, iterations, U, L, K):
    
    iterations = int(iterations); J = int(J) ; dt = T/J; t = np.linspace(0,T,J+1)[:,None];
            
     
    Z = np.random.randn(J,iterations); X = np.cumsum(Z,axis =0)
    
    X = np.vstack((np.zeros(iterations),X));
    
    sJ = S*np.exp((r-0.5*sigma**2)*t+sigma*np.sqrt(dt)*X);

    vJ = (((np.min(sJ, axis = 0)>L)*(np.max(sJ, axis = 0)<U))*np.exp(-r*T)*np.maximum(sJ[-1]-K, 0)).mean()

    return vJ