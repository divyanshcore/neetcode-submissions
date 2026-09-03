class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use set to remember the previously seen values

        store = set()
        for num in nums:
            if num in store:
                return True

            store.add(num)

        return False

        #TC =>O(N)
        #SC =>O(N)
                 


        