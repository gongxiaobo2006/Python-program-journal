
## 771. Jewels and Stones
### Problem description

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

### Example 1:
```
Input: J = "aA", S = "aAAbbbb"
Output: 3
```

### Example 2:
```
Input: J = "z", S = "ZZ"
Output: 0
```

### Note:
>S and J will consist of letters and have length at most 50.
>The characters in J are distinct.

```
class Solution:
    def numJewelsInStones(self, J, S):
        Jewels = list(J)
        Stones = list(S)
        count = 0 
        for Jew in Jewels:
	        for item in Stones:
		        if Jew == item:
			        count = count +1
		        else: 
			        pass
        return count
```

### Codes Explanation:
The problem here is to find the element from **J** contained in **S**. 
Under the circumstance, just traversal the list of **S** and compared with element in **J**.
And print out the value of counter so that the problem was solved. 






