class Solution:
    def isPalindrome(self, s: str) -> bool:
        #using two-pointers
       
        def isalphanum(c):
            return (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')

        lo, hi = 0, len(s)-1

        t = s.lower()

        while lo < hi:
            if not isalphanum(t[lo]):
                lo+=1
                continue

            if not isalphanum(t[hi]):
                hi-=1
                continue

            if t[lo] != t[hi]:
                return False
            lo+=1
            hi-=1

        return True

    #TC =>O(N)
    #SC =>O(1)            



        