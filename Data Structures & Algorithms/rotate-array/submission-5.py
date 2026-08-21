class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo+=1
                hi-=1

        n = len(nums)
        k = k%n
        helper(0, n-1)
        helper(0, k-1)
        helper(k, n-1)         
        