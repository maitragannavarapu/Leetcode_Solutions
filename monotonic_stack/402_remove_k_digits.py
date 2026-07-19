"""
LeetCode 402 - Remove K Digits

Pattern:
Monotonic Increasing Stack

Approach:
- Traverse each digit.
- While the top of the stack is greater than the current digit and removals remain,
  pop from the stack.
- Push the current digit.
- If removals still remain after traversal, remove digits from the end.
- Remove leading zeros.
- Return "0" if the result is empty.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for current in num:
            while stack and stack[-1] > current and k > 0:
                stack.pop()
                k -= 1
            stack.append(current)

        while k > 0:
            stack.pop()
            k -= 1
        result=''.join(stack)
        result=result.lstrip('0')
        if not result:
           return "0"
        return result
