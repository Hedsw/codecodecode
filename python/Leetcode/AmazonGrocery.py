import queue

"""
Ex. Person 1 - Enter Time: 10:00 AM, Exit Time: 10:10 AM
Ex. Person 2 - Enter Time: 09:00 AM, Exit Time: 09:15 AM
Ex. Person 3 - Enter Time: 09:30 AM, Exit Time: 09:45 AM

우선순위 큐(Priority Queue)는 들어간 순서에 상관없이
우선순위가 높은 데이터가 먼저 나오는 것 것을 말합니다. O(log n)
"""

class User:
    def __init__(self, customerID, enterTime, exitTime):
        self.customerID = customerID
        self.enterTime = enterTime
        self.exitTime = exitTime
        
class Users:
    def __init__(self):
        self.users = []
    
    def addUsers(self, user):
        self.users.append(user)
        
class CheckCapacity:
    def __init__(self):
        self.usersdict = {}
        self.enterQueue = queue.PriorityQueue(max = 100)
        self.exitQueue = queue.PriorityQueue(max = 100)
    
    def AppendQueue(self, User):
        self.usersdict[User.customerID] = [User.EnterTime, User.exitTime]  # To Check Current Users
        if self.enterQueue.full():
            self.usersdict.pop(User.customerID) # Delete Users in dictionary
            self.enterQueue.get() 
            self.enterQueue.pup(User.entertime, User)
        else:
             self.enterQueue.pup(User.entertime, User)
             
        if self.exitQueue.full():
            self.usersdict.pop(User.customerID) # Delete Users in dictionary
            self.exitQueue.get()
            self.exitQueue.pop(User.exitTime, User)
        else:
            self.exitQueue.pop(User.exitTime, User)
        
    