class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #sort both the strings and compare if both strings are same or not
        t1 = ''.join(sorted(list(s)))
        t2 = ''.join(sorted(list(t)))
        return t1 == t2
        
        #TC => O(nlogn + mlogm)
        #SC =>O(max(n,m))
        

        