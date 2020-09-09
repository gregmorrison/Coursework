clear;  
%clear out any previous definitions
data=load('periods.txt');
%import the data

f=figure;
%create a figure called f.

hold all
%the flag hold means we are going to add data to the plot, rather than replace data.  
% this is not necessary for this example, but may be needed when combining data.

set(f,'Visible','on');
%the chart will pop up if 'on' is selected.  You can use 'off' as well


plot(data(:,1),data(:,2),'-o','MarkerSize',10,'color','black');
% This is the actual plot.  
% the dash in front of the o connects the points.
%note that previously this was written as loglog(...) instead of plot.
% the loglog command does not work correctly in conjunction with the 
% hold on command above.  

title('period');
%writes to the top of the plot

box on
%puts a box all around the plot (instead of just x-y axes)

ax=gca;
% gca means "get current axes".  If you wnat to modify the axes, this is how.

ax.FontSize=12;
%sets the font size for the axes
set(ax,'Xscale','log')
set(ax,'Yscale','log')

xlabel('r');
ylabel('period');
%labels the axes 

saveas(gcf,'period','epsc');
%prints the figure to an eps file.  You should usually use eps instead of pdf if possible. 

hold off
