rng(2,'twister');  %don't initialize more than once!

kT=4.1;
zeta=20;
m=4.2;
dt=0.001;
nstep=10000;
nrun=10;


xvals=zeros(1,nstep);  %store values of average x
xsqvals=zeros(1,nstep);  %average x^2
vsqvals=zeros(1,nstep);
tvals=zeros(1,nstep);

disp('predicted timescale:')
disp(m/zeta)

for run=1:nrun

	x=0;
	t=0;
	xold=0;
	xnew=0;  %note!  reinitialize!


	for i=1:nstep
		R=randn()*sqrt(2*zeta*kT/dt);
		xnew=x;
		xnew=xnew+(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m);
		xnew=xnew+(R)*dt*dt/m/(1+zeta*dt/2/m);
        
		v=(xnew-xold)/(2*dt);

		xold=x;
		x=xnew;
		t=t+dt;


		xvals(i)=xvals(i)+x/nrun;
		xsqvals(i)=xsqvals(i)+x*x/nrun;
		vsqvals(i)=vsqvals(i)+v*v/nrun;
		tvals(i)=t;
	end
end


figure
hold on
plot(tvals,vsqvals,'r')
plot(tvals.*1.1,ones(1,nstep).*(kT/m),'k')

xlabel('t (us)')
ylabel('<v^2> (nm/us)^2')
legend({'simulation','equipartition'},'Location','southeast')
hold off



figure
hold on
plot(tvals,xsqvals,'r')
plot(tvals.*1.1,tvals.*(2*kT/zeta),'k')
xlabel('t (us)')
ylabel('<x^2> nm^2')
legend({'simulation','diffusion'},'Location','southeast')
hold off


figure
hold on
plot(tvals,xvals,'r')
xlabel('t (us)')
ylabel('<x> (nm)')
hold off







