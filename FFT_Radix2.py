import numpy as np
import matplotlib.pyplot as plt

def fft_radix2(x):
    n = len(x)
    if (n == 1):
        return x
    else: 
        xe = fft_radix2(x[0::2])
        xo = fft_radix2(x[1::2])
        # Once we have split the data into 1 point DFTs by separating the even and odd samples recursively
        #the samples will each be queued in the stack in bit reverse order. We then
        #combine the samples using 'butterflies' that are present in the signal flow graph. 
        #First stage will have 2 samples combined per butterfly, then the next stage will have 4, then 8 and so on. 
        #For example for a 8 sample signal we would need 3 stages of butterflys to reach the fully combined output of the samples of the DFT/FFT.
        
        w = np.exp(-2j*np.pi*np.arange(n)/n)
        X = np.concatenate([xe + w[:int(n/2)]*xo, xe + w[int(n/2):]*xo])
        return X 
     
     
#Test case
N = 64 #must be N = 2^i where i is integer
k = 3
x = np.sin(2*np.pi*(k/N)*np.arange(N))
X = fft_radix2(x)
#print("Final X", X)
plt.stem(abs(X))
plt.xlabel("Frequency bin k")
plt.ylabel("Magnitude")
plt.title("Simple FFT Radix-2")
    
    
