#https://leetcode.com/problems/perfect-squares/description/
#LeetCode 279. Perfect Squares

#author:peihan
#date: 05/15/2018


n = 12

#对小于16的square numbers进行筛选并储存
i3 =[]
for i in range(1,100):
	i2 = pow(i,2)
	i3.append(i2)
print(i3)	
squre_num =[]
for item in i3: 
	if n>=item:
		squre_num.append(item)
	else:
		pass
print(squre_num)

#使用square numbers组合出所需的数字
squre_num.reverse()
print(squre_num)

comb = n

i = 0 
result =[]

while comb >= squre_num[-1]: 
	if comb >= squre_num[i]:
		comb = comb - squre_num[i]
		result.append(squre_num[i])
	elif comb < squre_num[i]:
		i = i+1
		#squre_num.pop(0)
		#comb = n

print(result)
output = len(result)
print (output)










