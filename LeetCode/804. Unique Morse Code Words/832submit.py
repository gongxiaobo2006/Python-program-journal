class Solution:
    def uniqueMorseRepresentations(self, words):
        words = words
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        output = []
        for word in words:
            result = [0 for row in range(len(word))]
            chars = list(word)
            for i in range(len(chars)):
                chars[i] = int(ord(chars[i])) - 97
                result[i]= Morse[chars[i]]
            result="".join(result)
            output.append(result)
        output =set(output)
        output =len(output)
        return output