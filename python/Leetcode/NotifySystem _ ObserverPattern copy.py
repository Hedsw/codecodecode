from abc import ABCMeta, abstractmethod
class limitations(Enum):
    max_feed = 100000
    like = 100000
    person_limit = 1000

class user:
    def __init__(self, person_limit, feed, likes, message):
        self.person_limit = person_limit
        self.feed = feed
        self.message = message
        self.likes = likes
    
    def get_feed(self):
        return self.feed
    
    def get_message(self):
        return self._message
    
    def set_feed(self, feed):
        if self.feed > limitations.max_feed:
            print("over limitations")
            self.feed = limitations.max_feed
        else:
            self.feed = feed
        
    def set_message(self, message):
        self.message = message
    
class userA(user):
    def __init__(self, feed, likes, message):
        self.fpreference = []
        super(user, self).__init__(limitations.person_limit, feed, likes, message)

    def feedPreference(self, feed):
        self.fpreference.append(feed)
    
def main():
    a = userA(100, 1, "hello") # Initialized
    
    a.set_feed(1)
    a.set_message("helloworld")
        
# Template Method Pattern - Parent class에서 Skeleton Implementation을 하는 것이고
# Strategy Method Pattern - Commonality를 Parent class에서 구현하고 난 다음, Child Class에서 각각의 성능에 맞게 Modify를 진행함

# Abstract Class - doesn't support multiple inheritance.

# Interface - supports multiple inheritance.

# 하지만 파이썬에서는 Abstract와 Interface사이의 구분 없이 사용이 가능하다
# 파이썬은 Multiple Inheritance를 지원하기 때문


