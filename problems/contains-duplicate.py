# https://leetcode.com/problems/contains-duplicate/submissions/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        e = {}
        for i in nums:
            try:
                a = e[i] + 1
                return True
            except:
                e[i] = 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
