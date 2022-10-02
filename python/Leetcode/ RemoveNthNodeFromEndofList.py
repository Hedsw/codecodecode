# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head 
        
        for i in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next # start from first Node 
        
        slow.next = slow.next.next
        
        return head
        
            