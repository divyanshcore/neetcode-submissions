class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        temp = []
        s1, s2 = 0, 0
        while s1 < len(word1) or s2 < len(word2):
            if s1 < len(word1):
                temp.append(word1[s1])
                s1+=1
            
            if s2 < len(word2):
                temp.append(word2[s2])
                s2+=1

        return ''.join(temp)    
        