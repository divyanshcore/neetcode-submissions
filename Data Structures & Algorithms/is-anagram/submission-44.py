class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #put both the strings in hashmap and check both maps are same or not
        store1, store2 = {}, {}
        n = len(s)
        for i in range(n):
            store1[s[i]] = store1.get(s[i], 0)+1
            store2[t[i]] = store2.get(t[i], 0)+1

        return store1 == store2    

        #TC =>O(n)
        #SC =>O(n)

        
        