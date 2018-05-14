import glob
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.colors
from numpy import linalg as LA

#print(matrix_info)


#先将文件列表的顺序排列好
fcf = glob.glob('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/*.txt')
fcf = sorted(fcf)

#再将features读出来
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

# the methods of assignment 
'''
X = Xtrain 
XTX = np.dot(X.T,X) 
D,U = np.linalg.eig(XTX)
print(D)
print(U)
'''

#the methods to calculate covariance and eignevalue 
X = Xtrain
meanX=np.mean(X,axis=0) 
CtrX=X-meanX 
Xt = CtrX.T
matrix=np.dot(Xt,CtrX)
Cxx=1.0/(X.shape[0]-1)*matrix
D,U = LA.eig(Cxx)
print(D)
print(U)

eigen1=U[:,0:2]
print(eigen1)
t = np.dot(X,eigen1)
print(t)

axes = plt.gca()
axes.set_xlim([-10,10]) 
axes.set_ylim([-10,10]) 
pc1_x = t[0:20,0]
pc1_y = t[0:20,1]
pc2_x = t[20:40,0] 
pc2_y = t[20:40,1] 
plt.scatter(pc1_x, pc1_y, color='r') 
plt.scatter(pc2_x, pc2_y, color='k') 

plt.title('PC Scores')
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.show()











