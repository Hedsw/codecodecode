from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def getprice(self):
        pass
    
    def logic(self):
        pass

class Water(Product):
    def __init__(self, price):
        self.price = price
    
    def getprice(self):
        return self.price
    
class Coke(Product):
    def __init__(self, price):
        self.price = price
    
    def getprice(self):
        return self.price

class Coffee(Product):
    def __init__(self, price):
        self.price = price
        
    def getprice(self):
        return self.price

class Payment(ABC):
    @abstractmethod
    def checkout(self):
        pass
    def logic(self):
        self.checkout()

class CardPayment(Payment):
    def __init__(self, pay):
        self.pay = pay
        
class CashPayment(Payment):
    def __init__(self, pay):
        self.pay = pay 
    
    def checkout(self):
        return self.pay * 1.0

class VendingMachine:
    def __init__(self, capacity, pay):
        self.capacity = capacity
        self.pay = pay
        self.slots = {}
    
    def addproduct(self, idx, p):
        if len(self.slots) >= self.capacity:
            return False
        
        else:
            self.slot[idx] = p
            return True
    
    def getproduct(self, idx):
        result = self.slots[idx]
        if result:
            del self.slots[idx]
        
        return result
    
    def checkout(self, product, method):
        self.total = 0
        if method == 1:
            payment = CardPayment(5000)
            for i in range(product):
                self.total += payment.logic()
                
        elif method == 2:
            payment2 = CashPayment(5000)
            for i in range(product):
                self.total += payment2.logic()

def main():
    machine = VendingMachine()
    iteam1  = Water(1000)
    iteam2  = Coke(1000) # Add product
    machine.addproduct(1, iteam1.logic()) # get item's price
    machine.addproduct(2, iteam2.logic())
    
    machine.checkout(machine.getproduct, 2) # 2 is Cash, 1 is Card
    
 
    