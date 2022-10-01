# Given a sorted array of integers nums of size n. Every element appears twice expect for one. Return the element which appears only once.

def solve(n, nums):
    ans = 0
    for i in range(0, len(nums)):
        ans = ans ^ nums[i]
    return ans
