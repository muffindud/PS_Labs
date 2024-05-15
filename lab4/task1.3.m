c=imread('cat.jpg');
cc=c(1:end,1:end,:);
c2=cc-128;
figure;
imshow(c2);
