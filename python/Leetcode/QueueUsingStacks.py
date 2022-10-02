# Stack은 Last in First Out 방식이고, Insertion과 Deletion이 Same End에서 발생한다.
# Queue는 First in First out 방식이고, Insertion과 Deletion이 Different Ends에서 발생한다.
# https://www.geeksforgeeks.org/queue-using-stacks/ <-- 전체 문제..

# 이 방식에서는 두개의 Method가 있는데, enQeue는 Time Complexity O(n)이고, deQueue는 Time Complexity O(1)이다

# Method #1 방식..
# Input과 Output을 만들기.. 
# Time Complexity - Enqueue는 O(N), Pop Operation O(1)
# Space Complexity - O(N) Use of stack for storing values

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enQueue(self, x):
        
        # Move all element from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop

        # Push Item into self.s1
        self.s1.append(x)
        
        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
        
    def deQueue(self):
        
        if len(self.s1) == 0:
            print("Q is empty")
        
        x = self.s1[-1]
        self.s1.pop()
        return x

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
        
