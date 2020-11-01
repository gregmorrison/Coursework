clear all;

x=load('data.csv');
N=length(x);
t=1:N;
y=zeros(1,N);
y(1:N-1)=(x(1:N-1)+x(2:N))/2;
y(N)=(x(1)+x(N))/2;

xt=fft(x);
yt=fft(y);

px=abs(xt).^2;
py=abs(yt).^2;

figure
hold on
plot(t,x,'b');
plot(t,y,'r');
xlabel('T (dimensionless)');
ylabel('x(T), y(T)');
legend('x(t)','y(t)');
shg


figure
hold on
plot(t,px,'b')
xlabel=('f (dimensionless)');
ylabel=('power spectrum');
shg

figure
hold on
plot(t,py,'r')
xlabel=('f (dimensionless)');
ylabel=('filtered power spectrum');

