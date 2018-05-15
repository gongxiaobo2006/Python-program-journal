
#https://leetcode.com/problems/unique-morse-code-words/description/
#LeetCode 804. Unique Morse Code Words

#author:peihan
#date: 05/15/2018



Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

words = ["gin", "zen", "gig", "msg"]
output = []

for word in words:
	result = [0 for row in range(len(word))]

	chars = list(word)
	#print(chars)
	for i in range(len(chars)):
		chars[i] = int(ord(chars[i])) - 97 #ASCII code transformation
		#ord 函数可以把 字符转化成对应的ASCII码的数字,减去97则得到在Morse列表里的位置
		result[i]= Morse[chars[i]]
	#print(result)
	result = "".join(result)
	#print(result)
	output.append(result)

output =set(output)
output =len(output)
print(output)






