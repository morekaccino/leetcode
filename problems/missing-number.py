# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = nums.__len__()
        expected = n * (n + 1) // 2
        return expected - s

    def missingNumberXOR(self, nums: List[int]) -> int:
        r = 0
        for index, value in enumerate(nums):
            r ^= (index + 1) ^ value
        return r


