# With Observer Pattern
# 옵저버 패턴(observer pattern)은 객체의 상태 변화를 관찰하는 관찰자들, 
# 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴이다. 
# 주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다
class Config:
    def __init__(self, observers = []):
        self.observers = observers
        
    def get_all_observers(self):
        return self.observers
    
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        
    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass
        
    def notify(self, modifier = None):
        for observer in self.get_all_observers():
            if observer != modifier:
                observer.update(self)
        
class Core(Config):
    def __init__(self, id = 0):
        Config.__init__(self)
        self._id = id
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        self.notify()
        
#Observer
class User:
    def update(self, config):
        print("Config id: {} has been updated".format(config._id))

def main():
    c1 = Core(5)

    u1 = User()
    u2 = User()

    c1.attach(u1)
    c1.attach(u2)
    c1.id = 10
    
main()
#Config id: 10 has been updated
#Config id: 10 has been updated