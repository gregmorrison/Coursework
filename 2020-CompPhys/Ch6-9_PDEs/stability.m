eps=0.51;
max_eigenval=[];
for n=5:100
    M=zeros(n,n);
    %this is the slow way:  iterate over i and j and check if they are
    %nonzero, if so assign a value
%    for i=1:n
%        for j=1:n
%            if(i==j)
%                M(i,j)=1-2*eps;
%            end
%            if(abs(i-j)==1)
%                M(i,j)=eps;
%            end
%        end
    %this is the fast way, but relies on understanding how the data
    %structure works in matlab.  
    %[[ a b c d ] [ e f g h] [i j k l] [m n o p]] is a 4x4 array, but the 
    % 5th element of this "array" is e.  matlab organizes the array as a
    % single vector, which is faster computationally.  We can assign values
    % using this without looping.  
    M(1:1+n:end)=1-2*eps;
    M(2:n+1:end)=eps;
    M(n+1:1+n:end)=eps;
    if(n==5)
        disp(M)
    end
    lambdamax=max(abs(eig(M)));
    max_eigenval=[max_eigenval ; [n lambdamax]];
end

figure
plot(max_eigenval(:,1),max_eigenval(:,2),'-o')
xlabel('n')
ylabel('labmda_{max}')
