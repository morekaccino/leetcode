# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        original = nums.copy()
        nums.sort()
        start = 0
        end = nums.__len__() - 1
        while start <= end:
            if nums[start] + nums[end] == target:
                indices = [i for i, x in enumerate(original) if x == nums[start] or x == nums[end]]
                return list(set(indices))
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return []


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([3, 2, 3], 6)
    print(r)
