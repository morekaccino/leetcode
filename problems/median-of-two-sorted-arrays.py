# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[(len(nums) - 1) // 2] + nums[len(nums) // 2]) / 2
        return nums[len(nums) // 2]
