"""
Problem: 1979. Find Greatest Common Divisor of Array

Pattern:
- Math
- Euclidean Algorithm

Approach:
1. Find the smallest and largest elements.
2. Apply Euclid's algorithm.

Time Complexity: O(n)
Space Complexity: O(1)


"""
class Solution(object):
    def findGCD(self, nums):
        largest=nums[0]
        smallest=nums[0]
        for num in nums:
            if num>largest:
                largest=num
            if num<smallest:
                smallest=num
        while smallest>0:
            largest,smallest=smallest,largest%smallest
        return largest
