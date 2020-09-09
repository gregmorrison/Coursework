n=1000;  %columns
m=5000;   %rows


v1=ones(1,n);  % vector of ones
v2=0:m-1;    % range from 0..m-1
mat=ones(m,n)*3;  %matrix of constant values=3
product=0;



disp("the dimensions of mat are:")
disp(size(mat))

tic  %start the timer
for i=1:n
    for j=1:m
        product=product+v2(j)*mat(j,i)*v1(i);
    end
end
disp(strcat("the product was ",num2str(product)," using a loop"));
toc  %end the timer


disp("")


tic %star the timer
product=v2*mat*v1';  %multiply v2 * mat * v1^{Transpose}
disp(strcat("the product was ",num2str(product)," using the product method"));
toc %end the timer

