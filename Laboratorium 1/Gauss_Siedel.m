clear all;
clc;
%% Metoda Gaussa Seidela


A=[2 1 1 -1; 1 1 -1 1; 1 1 1 1; -1 2 -1 1]
b=[3 4 10 4]'
x=[1 1 1 1]'
n=size(x,1);
normVal=Inf; 
tol=1e-5; itr=1;

while normVal>tol
    x_old=x;

    for i=1:n

        sigma=0;

        for j=1:i-1
                sigma=sigma+A(i,j)*(j);
        end

        for j=i+1:n
                sigma=sigma+A(i,j)*x_old(j);
        end

        x(i)=(1/A(i,i))*(b(i)-sigma);
    end

    itr=itr+1;
    normVal=norm(x_old-x);
end
%%
fprintf('Rozwiazanie ukladu równań: \n%f\n%f\n%f\n%f in %d iterations',x,itr);