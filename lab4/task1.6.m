c=imread('cat.jpg');
cc=c(1:end,1:end,:);
c5=imadd(immultiply(cc,0.5),128);
figure;
imshow(c5);
