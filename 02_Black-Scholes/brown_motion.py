import numpy as np

def brown_motion(S, sigma, r, T, J, iterations, *args):

    if len(args)>0: np.random.seed(args);
    
    iterations = int(iterations); J = int(J) ; dt = T/J; t = np.linspace(0,T,J+1)[:,None];
    
    Z = np.random.randn(J,iterations); X = np.cumsum(Z,axis =0)
    
    X = np.vstack((np.zeros(iterations),X));
    
    sJ = S*np.exp((r-0.5*sigma**2)*t+sigma*np.sqrt(dt)*X);
    
    return t,sJ
