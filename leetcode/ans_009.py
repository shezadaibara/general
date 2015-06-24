"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        string = str(x)
        return string == string[::-1]