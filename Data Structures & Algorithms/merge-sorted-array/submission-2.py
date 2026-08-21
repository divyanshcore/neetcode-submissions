class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)-1
        p1, p2 = m-1, n-1
        
        while p1 >=0 and p2 >=0:
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1-=1
            else:
                nums1[k] = nums2[p2]
                p2-=1

            k-=1

        while p2>=0:
            nums1[k] = nums2[p2]
            p2-=1
            k-=1

        #TC =>O(N+M)
        #SC =>O(1)                         