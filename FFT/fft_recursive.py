import numpy as np
from math import pi

def fft(samples) :
    samples = np.array(samples, dtype=complex)
    N = samples.shape[0]

    if (N == 1) : 
        return samples
    if (N % 2 > 0) :
        print("O tamanho da amostra não é do tipo 2^k.")
        raise("Exiting...")
    Xe = fft(samples[::2])
    Xo = fft(samples[1::2])
    Wlk = np.exp((-2j * np.pi * np.arange(N)) / N)
    return np.concatenate([Xe + Wlk[:N // 2] * Xo,
                            Xe + Wlk[N // 2:] * Xo])
