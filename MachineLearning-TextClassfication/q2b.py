import glob
import numpy as np

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
      reload(sys)
      sys.setdefaultencoding(default_encoding)


fcf = glob.glob('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/*.txt')
fcf = sorted(fcf)

features = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/feature.txt','r')
message2 = features.read()
feature_list = message2.split(" ")

Xtrain = []
mylist = []

#13*40的矩阵
matrix = [None]*40  
for x in range(len(matrix)):  
    matrix[x] = [0]*13  
#print(matrix)


for n in range(len(feature_list)):
	print ("the current feature is " + feature_list[n])
	feature1 = feature_list[n]
	#print(fcf)

	for i in range(1,22):
		print(i)
		info = open(fcf[i],'r')
		messages = info.read()
		print(messages)
		message_each = messages
		count_Xtrain = message_each.count(feature1)
		print (count_Xtrain)
		print (" ")
		Xtrain.append(count_Xtrain)
		mylist.append(count_Xtrain)
		matrix(n,i) = count_Xtrain


	for i in range(23,36):
		print(i)
		info = open(fcf[i],'r')
		messages = info.read()
		print(messages)
		message_each = messages
		print (message_each.count(feature1))
		print (" ")

	for i in range(37,40):
		print(i)
		info = open(fcf[i],'r')
		messages = info.read()
		print(messages)
		message_each = messages
		print (message_each.count(feature1))
		print (" ")

	for i in range(40,51):
		print(i)
		info = open(fcf[i],'r')
		messages = info.read()
		print(messages)
		message_each = messages
		count_Xtest = message_each.count(feature1)
		#Xtest =[]
		#Xtest = count_Xtest
		print (count_Xtest)
		print (" ")

#print(Xtrain)
mat = np.array(mylist)
print (mat)


'''
feature_list = message2.split(" ")
print(feature_list)

i = 0 
for i in range(1,41):
	print(i)
	features = open(feature_list[i],'r')
	info = features.read()
	print(info)
	#message = text.read()
	#print (message1.count(feature1))
'''

'''
text=[]
for i in range(40):
	text = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/','r')
	text_list= text.read
text = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/01.txt','r')
message1 = text.read()
print (message1.count(feature1))
'''

'''
Xtrain = []
Xtrain = feature_list
print(Xtrain)
'''
'''
i = 0
for i in feature_list:
	Xtrain[0,i] = feature_list[i]
print(Xtrain)
'''

'''
text = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/01.txt','r')
message1 = text.read()
print (message1.count(feature1))
'''

