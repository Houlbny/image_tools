I=imread('./101res.png');  
siz=size(I);
I1=reshape(I,siz(1)*siz(2),siz(3));  % ÿ����ɫͨ����Ϊһ��
I1=double(I1);
[N,X]=hist(I1, [0:5:255]);% �����ҪС���ο�һ�㣬���������ٵ㣬���԰Ѳ����Ĵ󣬱���0:5:255
plot(X,N(:,[1]),'red','LineWidth',3);
xlim([0 255]);
hold on
plot(X,N(:,[2]),'green','LineWidth',3);
hold on
plot(X,N(:,[3]),'blue','LineWidth',3);
hold off
xlabel('Pixel values','fontsize', 20)
ylabel('Number of pixels','fontsize', 20)
legend('Location','northwest')
legend('R channel', 'G channel','B channel');