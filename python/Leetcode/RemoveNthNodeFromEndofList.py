# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = last = head
        count = 0
        
        while n != count:
            fast = fast.next
            count += 1
        
        if fast == None:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            last = last.next
        
        last.next = last.next.next
        
        return head
        
        # Fast 먼저 N에 도달하게 하고, 그 다음 Fast가 N의 끝이면 리턴하고
        # 아니면, Slow랑 Fast 동시 출발하면, Fast가 끝에 도달하면,
        # Slow자리가 N 자리가 됨
        
        