class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #we can use array of len 26 as map because it only contains lowercase letters

        map1 = [0]*26
        for i in range(len(s)):
            index1 = ord(s[i]) - ord('a')
            index2 = ord(t[i]) - ord('a')
            map1[index1]+=1
            map1[index2]-=1

        for num in map1:
            if num != 0:
                return False

        return True

        #TC =>O(n)
        #SC =>O(1)               


        
        