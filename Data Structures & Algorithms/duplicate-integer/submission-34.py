class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #check is current no is sen previously using set
        store = set()
        for num in nums:
            if num in store:
                return True
            store.add(num)

        return False     
        #TC =>O(N)
        #SC =>O(N)    