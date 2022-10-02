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
 
#HashMap O(n)
thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}

thisdict["Color"] = "Red" # Key랑 value 추가하고 싶을 때
thisdict['year'] += 1 # year +1 함
print(thisdict)

thisdict.update({"Color": "Blue"}) # Key는 놔두고 Value를 바꾸고 싶을 때
print(thisdict)

# 삭제시킬 때... Key, Value 다 삭제 할 때
#del thisdict["Model"]
print(thisdict)

for x in thisdict.values(): # Ford Mustang, 1964 출력
    if x == "Ford":
        print(x, " <-- is value")
      
for x in thisdict.keys(): # Brand, Model, Year 출력
    if x == "Brand":
        print("Key is Brand")
        print(thisdict[x], " <-- Value")

for x in thisdict:
    if thisdict[x] == "Ford": # Ford, Mustang, 1964 출력됨
        print(thisdict[x], "wow")
  

for key, values in thisdict.items():
    print(key, values) # 다 출력하는것  

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

# Dictionary를 Heap으로 넣어서 확인..
# Dict -> list -> heapify -> make it to dict again 
dict_1 = {11: 121, 2: 4, 5: 25, 3: 9}
# convert dictionary to list of tuples
di = list(dict_1.items()) 
heapq.heapify(di)
# converting heap to dictionary
di = dict(di)


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


stack.pop() 
