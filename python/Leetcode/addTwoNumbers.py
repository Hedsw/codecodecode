# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            value = carry%10
            cur.next = ListNode(value)
            cur = cur.next
            carry //= 10 # 만약 10을 넘어가는 숫자가 있으면,, 그 숫자를 다음 계산할 때 1 더해줌. 
        return dummy.next

    
'''
# Reverse Order Li L2를 리버스된 것을 되돌려서 Val를 다 합친 다음에.. 합친 숫자를 Reverse 시켜서 새로운 노드에 집어 넣으면 된다..
nextNode, nextNode2 = 0, 0
reverseL1, reverseL2 = None, None
list1, list2 = [], []
value1, value2 = 0, 0

returnRev = ListNode(None)

# Reverse l1 and l2 
while l1:
    nextNode = l1.next
    l1.next = reverseL1
    reverseL1 = l1
    l1 = nextNode
while l2:
    nextNode2 = l2.next
    l2.next = reverseL2
    reverseL2 = l2
    l2 = nextNode2

# add each linked list val to lists 
while reverseL1:
    list1.append(reverseL1.val)
    reverseL1 = reverseL1.next
while reverseL2:
    list2.append(reverseL2.val)
    reverseL2 = reverseL2.next

# add lists value together 
for i in range(len(list1)):
    value1 += list1[i]*math.pow(10,(len(list1)-1-i))
for i in range(len(list2)):
    value2 += list2[i]*math.pow(10,(len(list2)-1-i))

# make a value 
value = int(value1 + value2)
valueList = [int(x) for x in str(value)]

# make a new linked list
for i in range(len(valueList)):
    l1.val = valueList[:-(i+1)]
    l1 = l1.next
return l1
'''