f1 = 200;
f2 = 300;
f3 = 400;
Amp=1;
fs = 44100;
ts= 1/44100;
T=10;
t=0:ts:T;
y1 = sin(2*pi*f1*t);
y2 = sin(2*pi*f2*t);
y3 = sin(2*pi*f3*t);
yt = 0.3*y1 + 0.3*y2 + 0.3*y3;
sound(y1,fs)
pause(11)
sound(y2,fs)
pause(11)
sound(y3,fs)
pause(11)
sound(yt,fs)