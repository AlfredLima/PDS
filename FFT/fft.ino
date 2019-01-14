#include "arduinoFFT.h"
 
#define SAMPLES 128             //Must be a power of 2
#define SAMPLING_FREQUENCY 10000 //Hz, must be less than 10000 due to ADC
  
unsigned int sampling_period_us;
unsigned long microseconds;
 
double vReal[SAMPLES];
double vImag[SAMPLES];

arduinoFFT FFT = arduinoFFT(vReal,vImag,SAMPLES,SAMPLING_FREQUENCY);
 
void setup() {
    Serial.begin(115200); 
    sampling_period_us = round(1000000*(1.0/SAMPLING_FREQUENCY));
}
 
void loop() {

    while ( !Serial );

    for(int i=0; i<SAMPLES; i++)
    {
        microseconds = micros();    //Overflows after around 70 minutes!     
        vReal[i] = analogRead(0);
        vImag[i] = 0;
        while(micros() < (microseconds + sampling_period_us));
    }
    for(int i=0; i<(SAMPLES); i++){
      Serial.print(" ");
      Serial.print(vReal[i]);    //View only this line in serial plotter to visualize the bins
    }
    Serial.print("_");
    
    FFT.Windowing(vReal, SAMPLES, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD);
    FFT.ComplexToMagnitude(vReal, vImag, SAMPLES);

    for(int i=0; i<(SAMPLES/2); i++){
      Serial.print(vReal[i]);    //View only this line in serial plotter to visualize the bins
      Serial.print(" ");
    }
    Serial.println("");    
}