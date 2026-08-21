class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #remember the previously seen numbers
        store = {}
        for i, num in enumerate(numbers):
            if target-num in store:
                return [store[target-num]+1, i+1]
            store[num] = i

        #TC =>O(N)
        #SC =>O(N)        
        