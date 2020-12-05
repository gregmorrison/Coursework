rng(2,'twister');

N=20;
nstep=10000;
printstep=2000;
nprint=floor(nstep/printstep)+1;
nrun=1;

t=zeros(nprint,1);
avm=zeros(nprint,1);
ave=zeros(nprint,1);

J=0.01;
b=0;
pbc=true;

for run=1:nrun
   spins=zeros(N,N);
   m=0;
   for i=1:N
        for j=1:N
            if(rand()<.5)
                spins(i,j)=1;
                m=m+1;
            else
                spins(i,j)=-1;
                m=m-1;
            end
        end
   end
   e=get_init_energy(spins,J,b,N,pbc);
   
   
   for step=1:nstep
      s1=floor(N*rand())+1;
      s2=floor(N*rand())+1;
      enew=e+energy_difference(s1,s2,spins,J,b,N,pbc);
      if(metropolis(e,enew))
         spins(s1,s2)=-spins(s1,s2);
         if(spins(s1,s2)>0)
            m=m+2; 
         else
             m=m-2;
         end
      end
      e=enew;
      
      if(mod(step,printstep)==0)
          k=floor(step/printstep)+1;
          t(k)=step;
          avm(k)=avm(k)+abs(m)/N/N;
          ave(k)=ave(k)+e/J/N/N;
      end
   end
end

figure
plot(t,ave./nrun)
figure
plot(t,avm./nrun)


function x=metropolis(e,enew)
   if(e>enew)
       x=true;
   else
       if(rand()<exp(-(e-enew)))
           x=true;
       else
           x=false;
       end
   end
end


function e=get_init_energy(spins,J,b,N,pbc)
    e=0;
end


function de=energy_difference(s1,s2,spins,J,b,N,pbc)
    de=0;
end
