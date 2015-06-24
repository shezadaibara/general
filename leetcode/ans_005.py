"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists 
one unique longest palindromic substring.


HINT:
http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
An O(N) Solution (Manacher’s Algorithm)
"""


class Solution:
    # @param {string} s
    # @return {string}

    def longestPalindrome_n_sq(self, string):
        palindrome = ""
        for i in range(0, len(string) + 1):
            for j in range(i, len(string) + 1):
                temp = string[i:j]
#                 print temp
                if temp == temp[::-1] and len(temp) >= len(palindrome):
                    palindrome = temp
        return palindrome
    
    def process(self, s):
        ret = "^"
        for i in range(0, len(s)):
            ret += "#" + s[i]
        ret += "#$"
        return ret
    
    def longestPalindrome(self, string):
        T = "^#" + "#".join([s for s in string]) + "#$"
        P = [0 for i in range(0, len(T))]
        C = R = 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * C - i
            P[i] = min(R - i, P[i_mirror]) if R > i else 0
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]
        maxLen = 0
        centerIndex = 0
        for i in range(1, len(T) - 1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i

        return string[(centerIndex - 1 - maxLen) / 2: (centerIndex - 1 - maxLen) / 2 + maxLen]

if __name__ == '__main__':
    string = "abcaaasdabcba"
    s = Solution()
    ans = s.longestPalindrome(string)
    print ans
