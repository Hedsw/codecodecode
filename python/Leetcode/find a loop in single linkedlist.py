# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x, next_node = None):
        self.val = x
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, new_data):
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = ListNode(new_data)
        
        # 3. Make next of new Node as head
        new_node.next = self.head
        
        # 4. Move the head to point to new Node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The Given Privous node must in LinkedList")
        new_node = ListNode(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
            
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next
    
    def append(self, new_data):
        new_node = ListNode(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(list.next):
            last = last.next
        last.next = new_node
        
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
            
if __name__ == '__main__':    
    llist = LinkedList()
    llist.insert(3)
    llist.insert(2)
    llist.insert(0)
    llist.insert(-4)
    print(llist.printList())
    
    sol = Solution()
    if sol.hasCycle(llist):
        print("True")
    else:
        print("False")
    
