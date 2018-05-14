#codes for Perceptron with the full matrix Xtrain


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

#Y matrix
t = Xtrain
X1 = t[0:20, :]
X2 = t[20:40, :]
Y1=np.concatenate((np.ones((20,1)), X1), axis=1)
Y2=np.concatenate((np.ones((20,1)) * -1, -X2), axis=1)
Y_Xtest=np.concatenate((Y1, Y2), axis=0)


# Initialize
a = np.zeros((14, 1))
a_iter = a
k = 0

sum_wrong = 1
while sum_wrong > 0 and k < 1000:
    wrong = np.dot(Y_Xtest, a_iter) <= 0 
    sum_wrong = sum(wrong) 
    sum1 = sum(wrong * np.ones((1,14)) * Y_Xtest) 
    a_iter = a_iter + sum1.reshape(14,1)
    k = k + 1
a_Xtest = a_iter


a = (a_Xtest[1:14,:]).reshape(1,14 - 1)
gt = np.dot(a, Xtest.T)
gt = gt + (a_Xtest[0] * np.ones((1,10)))
Y_result = sum(gt < 0)

#get the mis match value
print(Y_result)
Y_true = [0,1,1,0,0,0,1,1,0,1]
mis_macth = sum((Y_result ^ Y_true))
print("the mis match number is "+str(mis_macth))

