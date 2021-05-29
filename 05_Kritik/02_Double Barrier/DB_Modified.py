import numpy as np
from math import log, sqrt, pi, exp

def pricing_cudo_moon(S, sigma, T, r, J, iterations, U, L, K):
    
    iterations = int(iterations); J = int(J) ; dt = T/J; t = np.linspace(0,T,J+1)[:,None];
            
   
    unU = np.random.uniform(size = iterations)
    unL = np.random.uniform(size = iterations)

    Z = np.random.randn(J,iterations); X = np.cumsum(Z,axis =0)

    X = np.vstack((np.zeros(iterations),X));

    sJ = S*np.exp((r-0.5*sigma**2)*t+sigma*np.sqrt(dt)*X);

    pL = np.exp(-2*((L-sJ[:-1])*(L-sJ[1:]))/(sigma**2*sJ[:-1]**2*dt))
    pU = np.exp(-2*((U-sJ[:-1])*(U-sJ[1:]))/(sigma**2*sJ[:-1]**2*dt))

    vJ = (((np.min(sJ, axis = 0)>L)*(np.max(sJ, axis = 0)<U))*(np.max(pL, axis = 0) < unL)*(np.max(pU, axis = 0) < unU)*np.exp(-r*T)*np.maximum(sJ[-1]-K, 0)).mean()

    return vJ
