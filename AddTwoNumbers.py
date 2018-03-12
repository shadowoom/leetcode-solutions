# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    carry = 0
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None and Solution.carry == 0:
            return None
        total = 0
        total += Solution.carry
        if l1 != None:
            total += l1.val
        if l2 != None:
            total += l2.val
        if total >= 10:
            total = total % 10
            Solution.carry = 1
        else:
            Solution.carry = 0
        newNode = ListNode(total)
        if l1 != None or l2 != None or Solution.carry == 1:
            if l1 == None and l2 != None:
                newNode.next = self.addTwoNumbers(None, l2.next)
            elif l1 != None and l2 == None:
                newNode.next = self.addTwoNumbers(l1.next, None)
            elif l1 != None and l2 != None:
                newNode.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                newNode.next = self.addTwoNumbers(None, None)
        else:
            newNode.next = None
        return newNode
        