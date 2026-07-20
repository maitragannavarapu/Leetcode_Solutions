"""
LeetCode 496 - Next Greater Element I

Pattern:
- Monotonic Stack (Decreasing Stack)
- Hash Map (Dictionary)

Approach:
1. Traverse nums2 from left to right.
2. Maintain a monotonically decreasing stack.
3. For each current element:
   - While the stack is not empty and the current element is greater than
     the top of the stack:
       - Pop the top element.
       - Record the current element as its next greater element in the dictionary.
   - Push the current element onto the stack.
4. After traversing nums2, the remaining elements in the stack do not have
   any greater element to their right, so map them to -1.
5. Traverse nums1 and use the dictionary to retrieve the next greater
   element for each number.
6. Return the resulting list.

Time Complexity:
- O(n + m)
  where:
  n = length of nums2
  m = length of nums1

Reason:
- Each element in nums2 is pushed onto the stack once and popped at most once.
- Looking up each element of nums1 in the dictionary takes O(1).

Space Complexity:
- O(n)

Reason:
- The stack and dictionary together store at most n elements.
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        nextgreater = {}

        for current in nums2:
            while stack and current > stack[-1]:
                removed = stack.pop()
                nextgreater[removed] = current
            stack.append(current)

        while stack:
            answer = stack.pop()
            nextgreater[answer] = -1

        answer = []

        for num in nums1:
            answer.append(nextgreater[num])

        return answer
