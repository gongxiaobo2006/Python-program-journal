


import glob
fcf = glob.glob('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/*.txt')
#print (fcf)


new = sorted(fcf)
#print (new)

text1 = open('/Users/Oliver/Desktop/香港大學研究生/Pattern recognition & machine learning/Assignment/Assignment1/Li_Peihan_3035492032_Ass1_ELEC6008/data/01.txt','r')
message = text1.read()
print (message)