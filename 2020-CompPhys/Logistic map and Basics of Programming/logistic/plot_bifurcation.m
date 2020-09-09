clear;  
%clear out any previous definitions
data=load('bifurcations_matlab.txt');
%import the data

f=figure;
%create a figure called f.

hold all
%the flag hold means we are going to add data to the plot, rather than replace data.  
% this is not necessary for this example, but may be needed when combining data.

set(f,'Visible','on');
%the chart will pop up if 'on' is selected.  You can use 'off' as well


plot(data(:,1),data(:,2:end),'.','MarkerSize',1,'color','black');
% This is the actual plot.  Only the first two aruments are required, the others optional.
% '.' refers to the plot markers being points.  You can use '+', for example.
% 'MarkerSize',1 choses the size of the plot markers
% 'color','black' choses the color.  

title('bifurcation diagram');
%writes to the top of the plot

box on
%puts a box all around the plot (instead of just x-y axes)

ax=gca;
% gca means "get current axes".  If you wnat to modify the axes, this is how.

ax.FontSize=12;
%sets the font size for the axes

xlabel('r');
ylabel('x_n');
%labels the axes 

saveas(gcf,'bifurcation','epsc');
%prints the figure to an eps file.  You should usually use eps instead of pdf if possible. 

hold off
