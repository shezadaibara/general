

class Solution:

    def reverse(self, x):
        rev = 0
        flag = False
        if x<0:
            x = abs(x)
            flag = True
        
        while x > 0:
            rev = rev * 10 + x % 10
            x = x / 10
        
        return -rev if flag else rev 

if __name__ == '__main__':
    x = -123
    s = Solution()
    res = s.reverse(x)
    print res
