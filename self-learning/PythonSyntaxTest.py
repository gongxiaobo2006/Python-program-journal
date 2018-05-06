#python syntax test


lang = "study python"
a = lang[0:]
b =lang[1:-1]
c = lang[0:-2]
d =lang[-1:]

str1 = "abcd"
str2 = "abcde"

import operator
operator.eq('hello', 'name')
print(len(lang))

print("Hello {0:.3} and {1:.2}".format("reatard","noob"))

print("you are a {var1} and {var2} boy".format(var1 = "noob", var2="faggot"))

varible1 = "stupid carry always farming without fighting"
varible2 ="1,2,3,4"
print(varible1.split(" "))
print(varible2.split(","))

e = " hello "
print(e)
print(e.strip())

f = "www.baidu.com"
g = f.split(".")
h =".".join(g)
i= "123"
j=i.encode(encoding='utf-8',errors='strict')


k =['1','2','www.baidu.com']

alst=[1,2,3,4,5,6,7,8]
word="google"
'''
l=alst[::-1] #reverse order
m=word[::-1] #reverse order
'''
#another revserse method
l=list(reversed(alst))
m=list(reversed(word))
#it is easy to notice the sequence of the m is shown in separated characters instead of word
n="".join(m)

#extend list
lista = [1,2,3,4,5]
listb = ['one','two','three']
#lista.extend(listb)
listc=lista+listb

#count the occuring times of elements
print(lista.count(6))

listd=["c","python","java","php","html"]
#the method of sort, just type in listd.sort() in command window with proper settings

#dictionary 
mydict = {} #the way to add content to dictionary
mydict['name'] = "peihan" 

# use tuple to create a dictionary
name = (["first","google"],["second","yahoo"])
website = dict(name)

#intersting tips: the usage is to replace information in HTML with dictonary of python
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"peihan","lang":"python"}
#then type in (temp % my) this command in command window

# the difference between copy and assign value to specifc varible

dict1 = {'language':'python','name':'peihan','hardware':'mac'}
dict2 = dict1 #this command cannot generate new dictionary
# use id(dict2) to find the location of dict2
dict3 = dict1.copy() #this command is to create a new dictionary with same value of dict1

#function define test

def func1(z):
    z=z+1






