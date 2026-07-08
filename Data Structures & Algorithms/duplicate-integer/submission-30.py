class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        table = {}
        for num in nums:
            table[num] = table.get(num, 0)+1

        for key, val in table.items():
            if val != 1:
                return True 

        return False 
        #TC =>O(N)
        #SC =>O(1)            