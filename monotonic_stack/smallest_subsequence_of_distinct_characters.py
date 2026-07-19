
"""
LeetCode 1081 - Smallest Subsequence of Distinct Characters

Pattern:
- Monotonic Stack
- Greedy
- Hash Map
- Set

Approach:
1. Store the last occurrence of every character.
2. Use a stack to build the answer.
3. Remove larger characters from the stack if they appear again later.
4. Use a set to avoid duplicate characters.
5. Return the characters in the stack as a string.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def smallestSubsequence(self, s):
        # Store the last occurrence index of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        # Stack to build the answer
        stack = []

        # Tracks characters already present in the stack
        seen = set()

        for i, ch in enumerate(s):

            # Skip duplicate characters
            if ch in seen:
                continue

            # Remove larger characters if they appear again later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            # Add the current character
            stack.append(ch)
            seen.add(ch)

        # Convert the stack into the required string
        return ''.join(stack)
