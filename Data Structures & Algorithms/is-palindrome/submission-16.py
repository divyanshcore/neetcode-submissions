class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        temp = []
        for c in t:
            if c.isalnum():
                temp.append(c)
     
        return temp == temp[::-1]

        #TC =>O(N)
        #SC =>O(N)        


        