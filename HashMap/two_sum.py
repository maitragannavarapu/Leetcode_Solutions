"""
Problem: Two Sum
LeetCode: #1
Difficulty: Easy

Pattern:
Hash Map

Approach:
Store each number and its index in a hash map.
For every element, calculate its complement (target - current number).
If the complement already exists in the hash map, return both indices.

Brute Force:
Time Complexity: O(n²)
Space Complexity: O(1)

Optimized:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# -------------------------
# Brute Force Solution
# -------------------------
class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# -------------------------
# Optimized Hash Map Solution
# -------------------------
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
