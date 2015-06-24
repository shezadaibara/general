"""
Given a string, find the length of the longest substring without repeating characters. 

For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
"""
import pdb

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        lastRepeating = -1
        longestSubstring = 0
        positions = {}
        for i in range(0, len(s)):
            if s[i] in positions and lastRepeating<positions[s[i]]:
                lastRepeating = positions[s[i]]
            if i-lastRepeating > longestSubstring:
                longestSubstring = i-lastRepeating
            positions[s[i]]=i
        return longestSubstring
            


if __name__ == '__main__':
    strings = ['ssssssaaaaaaxxyz', "abcbadbce"]
    sol = Solution()
    for s in strings:
        print s
        w = sol.lengthOfLongestSubstring(s)
        print s, w

