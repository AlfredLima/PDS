import numpy as np
from math import pi

def bitReverse(value, log2n):
	n = 0
	for _ in range(log2n):
		n = n<<1
		n = n|(value&1)
		value = value>>1
	return n

def fft_iterative(samples) :
    samples = np.array(samples, dtype=complex)
    N = samples.shape[0]
    
    if (N & (N-1)) or N == 0:
        print("O tamanho da amostra não é do tipo 2^k.")
        raise("Exiting...")

    fft = np.array(samples, dtype=complex)
    log2n = int(np.log2(N))
    
    for i in range(N):
        rev = bitReverse(i,log2n)
        fft[rev] = samples[i]

    J = complex(0,1)

    for s in range(1,log2n+1):
        m = 1<<s
        m2 = m>>1
        w = complex(1,0)
        wm = np.exp(J*np.pi/m2)

        for j in range(m2):
            for k in range(j,N,m):
                t = w * fft[k + m2]
                u = fft[k]

                fft[k] = u + t
                fft[k + m2] = u - t
            w *= wm

    return fft
