"""
The string "PAYPALISHIRING" is written in a zigzag pattern 
on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion 
given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, string, numRows):
        assert numRows > 0        # Must be a non-negative number
 
        # Handle a specific case, nRows be 1.
        # In such case, the input and output should be the same.
        if numRows == 1:
            return string
 
        # cache[i] stores the characters in the (i+1)th row,
        # in their original order.
        cache = [[] for _ in xrange(numRows)]
        position = 0    # The index of current row in cache.
        direction = +1  # The direction to find the next row.
 
        for element in string:
            cache[position].append(element)
 
            # If we are in the first row, we should find the next
            # row in an increasing order
            if position == 0:
                direction = +1
            # If we are in the last row, we should find the next
            # row in a decreasing order
            elif position == numRows - 1:
                direction = -1
 
            position += direction
 
        return "".join(["".join(row) for row in cache])

if __name__ == '__main__':
    numRows = 3
    string = "paypalishiring"
    s = Solution()
    res = s.convert(string, numRows)
    print res
    
            
