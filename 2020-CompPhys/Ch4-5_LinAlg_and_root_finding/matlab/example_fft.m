wall=60;  %signal from the wall, which we dont' care about
signal=200;  %true signal frequency
dt=.001;  %sampling rate (ms rate)

T=1;  %sample time
tvals=(1:(T/dt))*dt;

noiseScale=1;
x=1*sin(2*pi*tvals*signal)+.5*sin(2*pi*tvals*wall)+noiseScale*randn(size(tvals));


trans=fft(x);
mag=abs(trans);

figure 

plot(mag)
xlabel('frequency index (f in units of 1/dt)')
ylabel('X(f)')

figure()

plot(tvals,x)
xlabel('t (units of dt)')
ylabel('x(t)')



