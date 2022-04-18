# https://leetcode.com/problems/reorganize-string/
from itertools import permutations


class Solution:
    def reorganizeString(self, s: str) -> str:
        e = {}
        m = 0
        for i in s:
            try:
                e[i] += 1
                if e[i] > m:
                    m = e[i]
            except:
                e[i] = 1
        if 2 * m <= len(s) + 1:
            return self.stringMaker(s)
        else:
            return ""

    def stringMaker(self, s: str) -> str:
        for subset in permutations(s, len(s)):
            if self.checkString(subset):
                return "".join(subset)
        return ""
        # return "".join()

    def checkString(self, subset) -> bool:
        for i in range(len(subset) - 1):
            if subset[i] == subset[i + 1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.reorganizeString("aab"))
