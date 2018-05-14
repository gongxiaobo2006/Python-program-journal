
features = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/feature.txt','r')
message2 = features.read()
print(message2)

feature_list = message2.split()
feature1 = feature_list[7]
print(feature_list)

#text = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/23.txt','r')
#print(type(text))
#message1 = text.decode("utf8")
#message1 = text.read()
#print (message1.count(feature1))


text = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/01.txt','r',errors='ignore')
message1 = text.read()
print (message1.count(feature1))