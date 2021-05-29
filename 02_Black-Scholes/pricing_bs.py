import numpy as np
from brown_motion import brown_motion

def pricing_bs(S, sigma, T, r, J, iterations):
    
    sJ = brown_motion(S, sigma, r, T, J, iterations, 0)[1];
    
    return np.exp(-r*T)*np.mean(sJ)