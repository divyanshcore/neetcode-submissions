class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort both the strings and they should be equal
        s1, s2 = sorted(list(s)), sorted(list(t))

        return s1 == s2
        #TC =>O(nlogn + mlogm)
        #SC =>O(n+m)

        