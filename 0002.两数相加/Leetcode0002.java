/*
以下代码在2019年10月16日力扣通过执行：
执行用时：2 ms, 在所有 java 提交中击败了99.99%的用户
内存消耗 :43.4 MB, 在所有 java 提交中击败了88.80%的用户
原创作者： JustModesty谦逊
Bilibili：https://www.bilibili.com/video/av71404492/
Youtube：https://www.youtube.com/watch?v=dBhFLo_IOU0
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        int value = l1.val + l2.val;
        carry = value / 10;
        value = value % 10;
        ListNode head = new ListNode(value);
        ListNode pre = head;
        l1 = l1.next;
        l2 = l2.next;
        while (l1 != null && l2 != null) {
            value = l1.val + l2.val + carry;
            carry = value / 10;
            value = value % 10;
            ListNode node = new ListNode(value);
            pre.next = node;
            pre = node;
            l1 = l1.next;
            l2 = l2.next;
        }
        while (l1 != null) {
            value = l1.val + carry;
            carry = value / 10;
            value = value % 10;
            ListNode node = new ListNode(value);
            pre.next = node;
            pre = node;
            l1 = l1.next;
        }
        while (l2 != null) {
            value = l2.val + carry;
            carry = value / 10;
            value = value % 10;
            ListNode node = new ListNode(value);
            pre.next = node;
            pre = node;
            l2 = l2.next;
        }
        if (carry != 0) {
            ListNode node = new ListNode(carry);
            pre.next = node;
        }
        return head;
    }
}
