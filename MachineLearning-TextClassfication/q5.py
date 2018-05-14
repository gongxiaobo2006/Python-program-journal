



#import libraries
import glob
import numpy as np
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.colors
from numpy import linalg as LA
from cvxopt import solvers 
from cvxopt import matrix

#sorted all information
fcf = glob.glob('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/*.txt')
fcf = sorted(fcf)

#read features 
features = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/feature.txt','r')
message2 = features.read()
feature_list = message2.split()

matrix_info1 = np.zeros((40, len(feature_list)))
matrix_info2 = np.zeros((10, len(feature_list)))

for n in range(0,len(feature_list)):
	for i in range(0,40):
		print("第 " + str(i+1) + " message")
		text = open(fcf[i],'r',errors='ignore')
		message1 = text.read()
		count_info1 = message1.count(feature_list[n])
		print(message1)
		print(feature_list[n] + " 是当前正在比对的feature")
		print("出现次数为 " + str(count_info1))
		print(" ")
		matrix_info1[i,n] =  count_info1
		Xtrain = matrix_info1

	for a in range(0,10):
		b = a + 40
		print("第 " + str(b+1) + " message")
		text2 = open(fcf[b],'r',errors='ignore')
		message2 = text2.read()
		count_info2 = message2.count(feature_list[n])
		print(message2)
		print(feature_list[n] + " 是当前正在比对的feature")
		print("出现次数为 " + str(count_info2))
		print(" ")
		matrix_info2[a,n] =  count_info2
		Xtest = matrix_info2


print(Xtrain)
print(" ")
print(Xtest)
print(" ")


Y = np.zeros((40, 1))
Y[20:40,0]=1
print(Y)


#the methods to calculate covariance and eignevalue 
X = Xtrain
meanX=np.mean(X,axis=0) 
CtrX=X-meanX 
Xt = CtrX.T
matrix1=np.dot(Xt,CtrX)
Cxx=1.0/(X.shape[0]-1)*matrix1
D,U = LA.eig(Cxx)


eigen1=U[:,0:2]
t = np.dot(X,eigen1)

X1 = t[0:20,:]
X2 = t[20:40,:]

Y1=np.concatenate((np.ones((20,1)),X1), axis=1) 
Y2=np.concatenate((np.ones((20,1))*-1,-X2), axis=1) 
Y=np.concatenate((Y1,Y2), axis=0)

'''
#perceptron
# Initialize 
a=np.zeros((3,1))
# no. of misclassified samples 
sum_wrong=1
#Perceptron 
a_iter=a
k=0
while sum_wrong>0 and k<1000: 
		wrong=np.dot(Y,a_iter)<=0
		sum_wrong=sum(wrong)
		sum1=sum(wrong*np.ones((1,3))*Y) 
		a_iter=a_iter+sum1.reshape(3,1) 
		k=k+1
a_con=a_iter
x=np.arange(-10,100,10) 
y=-(a_con[0]+a_con[1]*x)/a_con[2]
t_test = np.dot(Xtest,eigen1)
gt = -(a_con[0]+a_con[1]*t_test)/a_con[2]
Y_test = np.zeros((1, 10))
print(Y_test)
#perceptron 
for i in range(1,10):
	if gt[i,0]>0 :
		print("it is class 2,and Y=1 ")
		Y_test[0,i] =1 
	else:
		print("it is class 1,and Y=0 ")
		Y_test[0,i] =0
'''


#hard margin support vector machine
A=matrix(np.concatenate((Y1,Y2), axis=0),tc='d') 
b=matrix(-1*np.ones((40,1)),tc='d') 
Q=matrix(2*np.eye(3),tc='d') 
q=matrix(np.zeros((3,1)),tc='d')
sol=solvers.qp(Q,q,A,b)
a_con=sol['x']
x=np.arange(-10,100,10) 
#print("x" + str(x))
y=-(a_con[0]+a_con[1]*x)/a_con[2]
#print(y)
t_test = np.dot(Xtest,eigen1)
gt = -(a_con[0]+a_con[1]*t_test)/a_con[2]
Y_test = np.zeros((1, 10))
print(Y_test)
#SVM
for i in range(1,10):
	if gt[i,0]<0 :
		print("it is class 2,and Y=1 ")
		Y_test[0,i] =1 
	else:
		print("it is class 1,and Y=0 ")
		Y_test[0,i] =0

print(Y_test)


Y_true = [0,1,1,0,0,0,1,1,0,1]
mis_match = Y_true-Y_test
print(mis_match)

axes = plt.gca()
axes.set_xlim([-5,5]) 
axes.set_ylim([-5,6]) 
pc1_x = t[0:20,0]
pc1_y = t[0:20,1]
pc2_x = t[20:40,0] 
pc2_y = t[20:40,1] 
xtest_x = t_test[:,0]
xtest_y = t_test[:,1]
plt.scatter(pc1_x, pc1_y, color='r') 
plt.scatter(pc2_x, pc2_y, color='k') 
plt.scatter(xtest_x,xtest_y, color='g')
plt.plot(x,y)
plt.title('PC Scores')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.show()




