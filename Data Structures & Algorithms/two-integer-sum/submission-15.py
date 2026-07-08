class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #check all the pairs
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

        return []   
        #TC =>O(n^2)
        #SC =>O(1)
                 

        