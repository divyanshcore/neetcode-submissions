class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #use set to remember the previously seen numbers

        prev = set()

        for num in nums:
            if num in prev:
                return True
            prev.add(num)

        return False
        #TC =>O(N)
        #SC =>O(N)
                   
        