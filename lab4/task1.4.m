c=imread('cat.jpg');
cc=c(1:end,1:end,:);
c3=imdivide(cc,2);
figure;
imshow(c3);
