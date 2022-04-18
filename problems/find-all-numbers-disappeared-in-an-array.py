# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        e = {}
        for i in range(1, nums.__len__() + 1):
            e[i] = 1
        for i in nums:
            try:
                del e[i]
            except:
                pass
        return list(e.keys())


if __name__ == "__main__":
    s = Solution()
    # print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(s.findDisappearedNumbers([1, 1]))
