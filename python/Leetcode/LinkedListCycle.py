# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Test File

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            fast = slow = head
            fast = fast.next

            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
        except:
            return False
    
   