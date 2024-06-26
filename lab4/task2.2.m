c=imread('cat.jpg');
cc=c(1:end,1:end,:);
subplot(1,2,1);
imshow(cc);
subplot(1,2,2);
I2=imadjust(cc, [.2 .3 0; .6 .7 1], []);
R=imhist(cc(:,:,1));
G=imhist(cc(:,:,2));
B=imhist(cc(:,:,3));
plot(R,'r');
hold on;
plot(G,'g');
plot(B,'b');
legend('Red','Green','Blue');
