# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        count = 0
        countNode = head
        front = back = head
        
        if not head:
            return True 
        if not head.next:
            return True
        
        while countNode:
            count += 1
            countNode = countNode.next
        
        halfCount = count / 2
        
        while halfCount > 0:
            back = back.next
            halfCount -= halfCount
        
        dummy = prev = ListNode()
        
        while back: 
            next = back.next
            back.next = prev
            prev = back
            back = next
        
        while head:
            if front.val == prev.val:
                front = front.next
                prev = prev.next
            else: # Not Palindrome Linked List 
                return False 
        return True
                