class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #sort the array and duplicates will side by side
        n = len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True

        return False
        #TC =>O(nlogn)    
        #SC =>O(n)    
        