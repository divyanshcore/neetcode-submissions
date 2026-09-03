class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort both the strings
        #check if both strings are exactly same or not

        s1 = sorted(s)
        t1 = sorted(t)

        return s1 == t1
        #TC => O(nlogn + mlogm)
        #SC => O(n+m){for sorting}
        