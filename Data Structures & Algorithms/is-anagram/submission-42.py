class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #using array of size 26 as map
        #this only works because string only contains
        #lowercase letters


        freq = [0]*26

        for i in range(len(s)):
            index1 = ord(s[i]) - ord('a')
            index2 = ord(t[i]) - ord('a')

            freq[index1]+=1
            freq[index2]-=1

        for num in freq:
            if num != 0:
                return False

        return True      
        #TC =>O(N)
        #SC =>O(1)      

        