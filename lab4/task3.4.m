c=imread('cat.jpg');
cc=c(1:end,1:end,:);
GS=rgb2gray(cc);
f=fspecial('laplacian');
cf2=filter2(f,GS);
f1=fspecial('log');
cf3=filter2(f1,GS);
figure;
subplot(1,2,1);
imshow(cf2/155);
subplot(1,2,2);
imshow(cf3/155);
