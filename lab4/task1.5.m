c=imread('cat.jpg');
cc=c(1:end,1:end,:);
c4=immultiply(cc,2);
figure;
imshow(c4);
