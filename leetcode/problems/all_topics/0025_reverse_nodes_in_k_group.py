from all_import import *

'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        previous = dummy

        count = 0
        current = head

        while current is not None:
            count += 1
            if count % k == 0:
                previous = self.reverseList(previous, current.next)
                current = previous.next
            else:
                current = current.next

        return dummy.next

    def reverseList(self, start, end):
        previous = start.next
        current = previous.next

        while current is not end:
            next_head = current.next
            current.next = start.next
            start.next = current
            current = next_head

        previous.next = end

        return previous
