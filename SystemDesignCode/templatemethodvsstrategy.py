
# Template Method Pattern - Parent class에서 Skeleton Implementation을 하는 것이고
# Strategy Method Pattern - Commonality를 Parent class에서 구현하고 난 다음, Child Class에서 각각의 성능에 맞게 Modify를 진행함
from abc import ABC, abstractmethod
# 둘 다 Behavioral Pattern임 

# Strategy Pattern
class Context():
    def __init__(self, strategy):
        self._strategy = strategy
        
    #strategy: Strategy  ## the strategy interface
    def do_commonlogic_download(self, p1, p2, p3):
        print("Describe Commonality Here")
        self._strategy.download(p1, p2, p3)

# Abstract method
class AbstractDownloader(ABC):
    @abstractmethod
    def download(p1, p2, p3):
        pass
    
class nasa_trmmRT_downloader(AbstractDownloader):
    def download(self, p1, p2, p3):
        print("ConCrete")


# Template Method Pattern - Parent class에서 Skeleton Implementation을 하는 것이고
# Strategy Method Pattern - Commonality를 Parent class에서 구현하고 난 다음, Child Class에서 각각의 성능에 맞게 Modify를 진행함

# Template Method Pattern
class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")
    
    @abstractmethod
    def required_operations1(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")
        
def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())