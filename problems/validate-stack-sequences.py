# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        s = Stack()
        i = 0
        j = 0
        while i != pushed.__len__():
            if s.peek() == popped[j]:
                s.pop()
                j += 1
            else:
                s.push(pushed[i])
                i += 1

        while j != popped.__len__():
            try:
                if s.pop() == popped[j]:
                    j += 1
                else:
                    return False
            except:
                return False

        if j == pushed.__len__():
            return True
        return False


class Stack:
    data = []

    def __init__(self):
        self.data = []

    def push(self, a: int):
        self.data.append(a)

    def pop(self) -> int:
        return self.data.pop()

    def peek(self) -> int:
        return self.data[-1] if self.data.__len__() > 0 else None

    def __len__(self):
        return self.data.__len__()


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
