a=zeros(256,256);
a(78:178,78:178)=1;
figure;
subplot(1,2,1);
imshow(a);
af=fftshift(fft2(a));
subplot(1,2,2);
imshow(af);
