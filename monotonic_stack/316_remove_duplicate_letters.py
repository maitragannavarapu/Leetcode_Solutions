"""
LeetCode 316 - Remove Duplicate Letters

Pattern:
- Monotonic Stack
- Greedy
- Hash Map
- Set

Approach:
1. Store the last occurrence index of every character.
2. Iterate through the string.
3. Skip characters that are already included in the result.
4. While the current character is smaller than the top of the stack
   and the top character appears again later, remove it from the stack.
5. Push the current character onto the stack and mark it as seen.
6. Join the stack to form the lexicographically smallest string.

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)
