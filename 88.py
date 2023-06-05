from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = [10**10] * n
        for i in nums2:
            for idx, j in enumerate(nums1):
                if i <= j:
                    nums1[idx+1:] = nums1[idx:len(nums1)-1]
                    nums1[idx]=i
                    break
                else:
                    if j == 10**10:
                        nums1[idx] = i
                        break