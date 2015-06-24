"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""



class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum_(self, nums, target):
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                if a+b == target:
                    return i+1, i+j+2
    
    def twoSum(self, nums, target):
        map = {}
        for i, a in enumerate(nums):
            try:
                j = map[a]
                return j, i+1
            except KeyError:
                diff = target-a
                map[diff] = i+1

def main():
    target = 80
    nums = [10, 20, 30, 40, 50]
    s = Solution()
    print s.twoSum(nums, target)