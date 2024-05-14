c=imread('cat.jpg');
cc=c(1:end,1:end,:);
c1=imadd(cc,128);
figure;
imshow(c1);
title('Image with added brightness');
