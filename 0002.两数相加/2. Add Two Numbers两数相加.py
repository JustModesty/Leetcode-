"""
以下代码在2019年10月16日可以正常执行：
执行用时：52 ms, 在所有 python 提交中击败了94.51%的用户
内存消耗 :11.9 MB, 在所有 python 提交中击败了16.63%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        value = l1.val + l2.val
        carry = value // 10
        value = value % 10
        head = ListNode(value)
        pre = head
        l1 = l1.next
        l2 = l2.next
        # 如果两个链表的当前位都不为空
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = value // 10
            value = value % 10
            node = ListNode(value)
            pre.next = node
            pre = node
            l1 = l1.next
            l2 = l2.next
        # 走到这一步，说明l1、l2至少有一个指向为空
        while l1:
            value = l1.val + carry
            carry = value // 10
            value = value % 10
            node = ListNode(value)
            pre.next = node
            pre = node
            l1 = l1.next
        while l2:
            value = l2.val + carry
            carry = value // 10
            value = value % 10
            node = ListNode(value)
            pre.next = node
            pre = node
            l2 = l2.next
        # 直到两个都为空了，继续判断carry是否有进位，如果carry不为0，则新建一个节点
        if carry:
            node = ListNode(carry)
            pre.next = node
        return head