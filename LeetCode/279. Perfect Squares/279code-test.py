#https://leetcode.com/problems/perfect-squares/description/
#LeetCode 279. Perfect Squares

#author:peihan
#date: 05/15/2018

n = 12
if n < 2:
	print (n)


lst = []
i = 1 
while i*i <= n:
	lst.append(i*i)
	i += 1
print (lst)

cnt = 0
toCheck = {n}
flag = 1
#while toCheck:
while flag==1:
	cnt += 1
	temp = set()
	for x in toCheck:
		for y in lst:
			print("      此时的y是  "+str(y))
			if x == y:
				print(cnt)
				flag = 0
			if x < y:
				break
			temp.add(x-y)
			print('此时temp是'+str(temp))
	toCheck = temp #此时更新的temp则是树的新的一层
	print(temp)

#print(cnt)







