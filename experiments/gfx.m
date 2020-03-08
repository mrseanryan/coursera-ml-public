graphics_toolkit('gnuplot')
graphics_toolkit

%% Initialization
clear ; close all; clc

figure(1)
subplot(1,3,1)
t = [0:0.01:0.98];
y1 = sin(2*pi * 4 * t);
plot(t, y1);
hold on;
y2 = cos(2*pi*4*t);
plot(t, y2, 'r'); % r = red

axis([0.25 0.75 -0.5 0.5]);

xlabel('time');
ylabel('value');
legend('sin', 'cos');
title('plot-1');

hold off;

subplot(1,3,2);
A = magic(5);
%heatmap of A
imagesc(A), colorbar, colormap ocean;

subplot(1,3,3);
B = randn(25);
%heatmap
imagesc(B), colorbar;

figure(2);
subplot(1,1,1);
t = [-100:1.00:100];
y = 80 + 1.8 * t;
plot(t, y, 'r');
hold on;
y2 = 80 + 1.8 * t + 1.5 * t.^2;
plot(t, y2, 'g');
y3 = 80 + 0.8 * t + 0.5 * t.^2 + 0.2 * t.^3;
plot(t, y3, 'b');
y4 = 80 + 0.8 * t + 0.5 * t.^2 + 0.2 * t.^3 + 0.3 * t.^4;
plot(t, y4, 'm');
legend('linear','quadratic','cubic', '4th');
axis([-50 50 -10.^3 10.^4]);

function y3 = y3_calc (x)
    y3 = 80 + 0.8 * x + 0.5 * x.^2 + 0.2 * x.^3;
endfunction

%make a nice 3-D plot:
%y3 has nice range x=-20 -> 40
x_min=-20;
x_max=40;
x_range = x_max - x_min;
D=zeros(100,100);
for i=1:100,
    for j=1:100,

    half_from_center = 100 / 2;
    i_from_center = i - half_from_center;
    j_from_center = j - half_from_center;

    d_from_center = (i_from_center.^2 + j_from_center.^2) / half_from_center;
    x =  ((half_from_center - d_from_center) * x_range) + x_min;

    D(int32(i),int32(j)) = y3_calc(x);

    end
end
figure
surf(D)
figure
contour(D)
