class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #another way could be put all the no's in a set 
        #& check size of it compared to nums
        store = set(nums)
        return not(len(nums) == len(store))
        #TC =>O(N)
        #SC =>O(N)

        #set to check whether current no is previously seen or not
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        #TC =>O(N)
        #SC =>O(N)         

        #using frequency table 
        table = {}
        for num in nums:
            table[num] = table.get(num, 0)+1

        for key, val in table.items():
            if val != 1:
                return True 

        return False 
        #TC =>O(N)
        #SC =>O(1)            