class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using hashmap to remember previously seen values

        table = {}

        for i, num in enumerate(nums):
            if target-num in table:
                return [table[target-num], i]
            
            table[num] = i    

        #TC =>O(N)
        #SC =>O(N)        
        