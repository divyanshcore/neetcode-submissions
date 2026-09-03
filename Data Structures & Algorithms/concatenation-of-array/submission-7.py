class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        #amateur brute force
        n = len(nums)
        res = [0]*(2*n)
        for i in range(n):
            res[i] = nums[i]

        for i in range(n):
            res[i+n] = nums[i]
        
        return res
        #TC =>O(N)
        #SC =>O(N)
        
