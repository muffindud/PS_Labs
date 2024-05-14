c=imread('cat.jpg');
cc=c(1:end,1:end,:);
GS=rgb2gray(cc);
c_sp=imnoise(GS,'salt & pepper');
imshow(c_sp);
