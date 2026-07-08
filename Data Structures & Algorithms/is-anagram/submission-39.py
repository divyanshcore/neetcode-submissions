class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #as we both 's' and 't' contain only lowercase letters
        # we can use array of 26 size as freq table 

        freq = [0]*26
        for i in range(len(s)):
            index1 = ord(s[i]) - ord('a')
            index2 = ord(t[i]) - ord('a')
            freq[index1]+=1
            freq[index2]-=1

        for val in freq:
            if val != 0:
                return False

        return True   
        #TC =>O(N)
        #SC =>O(1)

            
