import serial, time
import numpy as np
import matplotlib.pyplot as plt
from fft_recursive import fft
from fft_iterative import fft_iterative

SERIAL_PORT = '/dev/ttyACM0'
SERIAL_RATE = 115200
SAMPLING_RATE = 1000
SAMPLES = 128

def creating_freq() :
    k = np.arange(SAMPLES)
    T = SAMPLES / SAMPLING_RATE
    freq = k / T
    freq = freq[range(SAMPLES//2)]
    return freq

def update_plot(fig, plt1, plt2, plt3, plt4, signal_data, t, fft_ard, freq, fft_py, fft_py_recursive) :
    plt1.set_ydata(signal_data)
    plt2.set_ydata(fft_ard) # plotting the spectrum
    plt3.set_ydata(abs(fft_py)) # plotting the spectrum
    plt4.set_ydata(abs(fft_py_recursive)) # plotting the spectrum
    fig.canvas.draw()

def init_plot(fig, ax, t, freq) :
    plt1, = ax[0].plot(t, np.zeros(len(t)))
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[0].set_ylim((0, 1023))
    plt2, = ax[1].plot(freq , np.zeros(len(freq)),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|FFT_ARD|')
    ax[1].set_ylim((0, 500))
    plt3, = ax[2].plot(freq , np.zeros(len(freq)),'g') # plotting the spectrum
    ax[2].set_xlabel('Freq (Hz)')
    ax[2].set_ylabel('|FFT_ITERATIVE|')
    ax[2].set_ylim((0, 500))
    plt4, = ax[3].plot(freq , np.zeros(len(freq)),'y') # plotting the spectrum
    ax[3].set_xlabel('Freq (Hz)')
    ax[3].set_ylabel('|FFT_RECURSIVE|')
    ax[3].set_ylim((0, 500))
    return [plt1, plt2, plt3, plt4]


def main():
    plt.ion()
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    freq = creating_freq()
    t = np.arange(0,1, 1.0/SAMPLING_RATE )
    t = t[:SAMPLES]
    fig, ax = plt.subplots(4, 1)
    figManager = plt.get_current_fig_manager()
    figManager.full_screen_toggle()
    [plt1, plt2, plt3, plt4] = init_plot(fig, ax, t, freq)
    while True:
        reading = ser.readline()
        reading = str(reading)
        arr = reading.split("_")
        if (len(arr) == 1) : continue
        try : 
            signal_data = arr[0].split(" ")[1:]
            signal_data = list(map(float, signal_data))
            fft_ard = arr[1].split(" ")[:-1]
            fft_ard = list(map(float, fft_ard))
        except :
            continue
        if (len(signal_data) != SAMPLES) : continue
        if (len(fft_ard) != SAMPLES//2) : continue
        fft_py_recursive = fft(np.array(signal_data)) / SAMPLES
        fft_py_recursive = fft_py_recursive[:SAMPLES//2]
        fft_py = fft_iterative(np.array(signal_data)) / SAMPLES
        fft_py = fft_py[:SAMPLES//2]
        update_plot(fig, plt1, plt2, plt3, plt4, signal_data, t, fft_ard, freq, fft_py, fft_py_recursive)


if __name__ == "__main__":
    main()