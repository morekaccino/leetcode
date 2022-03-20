# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # preperation
        S = ""
        for i in s:
            S += '#{}'.format(i)
        S = S + '#'
        # a = [0] * len(S)

        res = ''
        i = 0
        while i < len(S):
            temp = self.longestPalindromeAt(S, i)
            if len(temp) > len(res):
                res = temp
            # a[i] = (len(temp) - 1) // 2
            i += 1 #max(((len(temp) - 1) // 2) - 1, 1)

        return res.replace('#', '')

    def isPalindrome(self, s: str) -> bool:
        # odd
        if len(s) % 2 == 1:
            a = s[:len(s) // 2]
            b = s[len(s) // 2 + 1:]
            return list(a) == list(reversed(b))

        # even
        else:
            a = s[:(len(s) // 2)]
            b = s[(len(s) // 2):]
            return list(a) == list(reversed(b))

    def longestPalindromeAt(self, s: str, a: int) -> str:
        res = s[a]
        i = 1
        while a - i >= 0 and a + i < len(s):
            temp_res = s[a - i: a + i + 1]
            if self.isPalindrome(temp_res):
                res = temp_res
                i += 1
            else:
                return res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('aaaa'))
