c=imread('cat.jpg');
cc=c(1:end,1:end,:);
IG=rgb2gray(cc);
c_sp=imnoise(IG,'salt & pepper');
cf=fftshift(fft2(c_sp));
b=zeros(1024,1024);
b(512-256:512+256,512-256:512+256)=1
cf1=cf.*b;
cf2=ifft2(cf1);
figure;
imshow(cf2/155);
