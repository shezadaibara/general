"""
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str(self.val)

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = ListNode(0)
        result_head = result
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            result.val = total % 10 
            l1 = l1.next
            l2 = l2.next
            if carry or l1 or l2:
                result.next = ListNode(carry)
                result = result.next
        while l1:
            total = l1.val + carry
            carry = total // 10
            result.val = total % 10 
            l1 = l1.next
            if carry or l1:
                result.next = ListNode(carry)
                result = result.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            result.val = total % 10 
            l2 = l2.next
            if carry or l2:
                result.next = ListNode(carry)
                result = result.next

        return result_head

    
    def addTwoNumbers_old(self, l1, l2):
        carry = 0
        result = ListNode(0)
        result_head = result
        while l1 and l2:
#             import pdb;pdb.set_trace()
            total = l1.val + l2.val
            carry = result.val
            result.val = (total + carry) % 10
            result.next = ListNode(total // 10)
            l1 = l1.next
            l2 = l2.next
            print result
            result = result.next
        while l1:
            total = l1.val
            carry = result.val
            result.val = (total + carry) % 10
            result.next = ListNode(total // 10)
            l1 = l1.next
            result = result.next
        while l2:
            total = l2.val
            carry = result.val
            result.val = (total + carry) % 10
            result.next = ListNode(total // 10)
            l2 = l2.next
            result = result.next
        
        return result_head
    
    def addTwoNumbers_s(self, l1, l2):
        carry = 0
        result = []
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            current = ListNode(total % 10)
            result.append(current)
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + carry
            carry = total // 10
            current = ListNode(total % 10)
            result.append(current)
            l1 = l1.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            current = ListNode(total % 10)
            result.append(current)
            l2 = l2.next
        
        if carry:
            current = ListNode(carry)
            result.append(current)
            
        
        for i, node in enumerate(result):
            if i == 0:
                try:
                    node.next = result[i+1]
                except IndexError:
                    pass
                head = result[i]
            else:
                try:
                    node.next = result[i+1]
                except IndexError:
                    pass
        return head


def print_l(res):
    res_str = ''
    while res:
        res_str += " {} --> ".format(res.val)
        res = res.next
    print res_str

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    print_l(l1)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print_l(l2)
    
    l1 = ListNode(5)
    l2 = ListNode(5)
    
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    print_l(res)
    