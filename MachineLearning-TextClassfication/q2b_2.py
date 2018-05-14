import glob
import numpy as np


#print(matrix_info)


#先将文件列表的顺序排列好
fcf = glob.glob('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/*.txt')
fcf = sorted(fcf)

#再将features读出来
features = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/feature.txt','r')
message2 = features.read()
feature_list = message2.split(" ")

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
X = Xtrain

#X[0] = Xtrain[0:20,0]
#X[1] = Xtrain[20:40,7]
#print(X)










