import heapq
listForTree = [2,1,3,4,5,6,7,8,9,10,11,12,13,14,16,17]    
heapq.heapify(listForTree)             # for a min heap
print(heapq.heappop(listForTree), " Min")     # pop from minheap
# 이거 하면 1이 출력
# Time comp - O(logn)

listForTree = [2,1,3,4,5,6,7,8,9,10,11,12,13,14,16,17]
heapq._heapify_max(listForTree)        # for a maxheap!!    
print(heapq._heappop_max(listForTree), " Max") # pop from maxheap
# 이거하면 17 출력
# Time comp - O(logn)

################################################################################

# 파이썬 파이너리 써치..
import bisect
    li = [1, 3, 4, 4, 4, 6, 7]
    i = 4
    print(bisect.bisect_left(li, i))
    print(bisect.bisect_right(li, i))
    로 하면.. 2, 5가 나옴 
    구현한다면....

    # Check base case O(logN)
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

####################################################################################################
#HashMap O(n)
if __name__ == '__main__':
    thisdict = {
        'bob': 1,
        'alice': 2,
        'jack': 3,
    }
    print(thisdict['bob'])
    thisdict['bob'] += 1
    thisdict['newbob'] = 1
    thisdict['newbob'] += 1
    for x in thisdict:
        print(x)
    for x in thisdict:
        print(thisdict[x])

####################################################################################################
# Heap 
# 작은 순서로 팝하기 Insert - O(logn), Pop - O(1)
_list = [11,4,5,6,2,3,8,10,9]
heapq.heapify(_list)
for i in range(5):
    poped = heapq.heappop(_list)
    print(poped)

# 큰 순서로 팝하기 Insert - O(logn), Pop - O(1)
_list = [11,4,5,6,2,3,8,10,9]
heapq._heapify_max(_list)
for i in range(5):
    minpop = heapq._heappop_max(_list)
    print(minpop)


####################################################################################################
# stack - Last in First out (LIFO)
# Queue - First in First out (FIFO)
"""
그냥 사용할때는.. 
stack = [3, 4, 5]
stack.append(6)
stack.pop() 

만드는 법..
class Stack:
    def __init__(self):
        self.stack = []
    
    def isempty(self):
        return len(self.stack) == 0
    
    def push(self, p):
        self.stack.append(p)
    
    def pop(self):
        return self.stack.pop()
"""
from queue import Queue

q = Queue(maxsize = 3)
# qsize() give the maxsize of the Queue
q.qsize()

# Adding of element to queue
q.put('a')

# Return Boolean for Full Queue
q.full()

# Removing element from Queue
q.get()

# Return Boolean for Empty Queue
q.empty()
