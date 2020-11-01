N = 128;
tau = 1; % Time increment
t = (0:(N-1))*tau;
fNy = 1/(2*tau); % Nyquist frequency 
df = fNy/16;
y = zeros(1,N);
ya = zeros(1,N);
for freq=df:df:fNy
  y = y + sin(2*pi*t*freq);
end
ya(1:N-1) = 0.5*(y(1:N-1) + y(2:N) );
ya(N) = 0.5*(y(N) + y(1));

yt=fft(y);
yat=fft(ya);
f=(0:N/2-1)/(N*tau);
spect=abs(yt(1:N/2)).^2;
specta=abs(yat(1:N/2)).^2;
plot(f,specta)