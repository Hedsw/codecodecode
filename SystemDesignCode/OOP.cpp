// Abstraction, Encapsulation, Inheritance, Polymorphism
// Abstraction - 추상화 (Keyword: 필요한 정보만 보여주고, 다른 정보들은 숨긴다)
// Encapsulation - 캡슐화  (Keyword: Getter and Setter로 데이터 접근하도록해서, 외부로부터 정보를 보호하는 방법)
// Inheritance: 상속 (Keyword: Code Reusability를 높인다)
// Polymolphism: 다형성 
// - Overloading(Compile-time polymorphism), 
// - Overriding(Run-Time Polymorphism)
"""
Time Complexity
Hashmap - O(1), Worst Case O(n)
Stack - O(1)
Queue - O(1) 
MergeSort, HeapSort, QuickSort - O(nlog(n)) -> Average 
Binary Search - O(logn), Best-Time - O(1) - (https://www.geeksforgeeks.org/python-program-for-binary-search/)
"""
/*
Abstraction is the concept of object-oriented programming that "shows" only essential attributes 
and "hides" unnecessary information. The main purpose of abstraction is hiding the unnecessary details 
from the users. Abstraction is selecting data from a larger pool to show only relevant details of the object to the user. 
It helps in reducing programming complexity and efforts. It is one of the most important concepts of OOPs.

In this case the variables myNum1, myNum2 and myNum3 are private, thereby in accessible to any code other than the class Summation. 
In this example the variables are set to values passed in as arguments to the sum method

추상화는 필수 속성만 "보여주고" 불필요한 정보를 "숨긴다"는 객체 지향 프로그래밍의 개념입니다. 추상화의 주요 목적은 사용자에게 불필요한 세부 사항을 숨기는 것입니다. 
추상화는 더 큰 풀에서 데이터를 선택하여 사용자에게 개체의 관련 세부 정보만 표시하는 것입니다. 
프로그래밍 복잡성과 노력을 줄이는 데 도움이 됩니다. OOP의 가장 중요한 개념 중 하나입니다.
아래와 같이 할 경우.. Private에 설정된 myNum1, myNum2, myNum3는 보여줄 필요가 없음. 우리가 보여주고 싶은 sum 된 결과만 보여줄 수 있음

아래의 예시가 완전히 좋은 예시는 아니지만 Abstraction을 보여주는 좋은 예
Example of Abstraction:
*/
#include <iostream> 
using namespace std; 

class Summation { 
   private: 
      // private variables 
      int myNum1, myNum2, myNum3 
   public: 
      void sum(int inNum1, int inNum2) 
      { 
          myNum1 = inNum1; 
          myNum2 = inNum2; 
          myNum3 = myNum1 + myNum2; 
          cout << "Sum of the two number is : " << myNum3< <endl; 
      } 
}; 
int main() { 
    Summation mySum; 
    mySum.sum(5, 4); 
    return 0; 
} 


// Encapsulation - 캡슐화  (Keyword: Getter and Setter로 데이터 접근하도록해서, 외부로부터 정보를 보호하는 방법)
/*
Encapsulation is a method to hide the data in a single entity or unit along with a method to protect information from outside.
Also, encapsulation is a method of making a complex system easier to handle for end users. 
The user need not worry about internal details and complexities of the system. Encapsulation is a process of wrapping the data 
and the code, that operate on the data into a single entity. You can assume it as a protective wrapper 
that stops random access of code defined outside that wrapper.

캡슐화는 최종 사용자가 복잡한 시스템을 더 쉽게 처리할 수 있도록 하는 방법입니다. 캡슐화는 외부로부터 정보를 보호하는 방법과 함께 단일 개체 또는 단위의 데이터를 숨기는 방법입니다.
사용자는 시스템의 내부 세부 사항과 복잡성에 대해 걱정할 필요가 없습니다. 
캡슐화는 데이터와 데이터에 대해 작동하는 코드를 단일 엔터티로 래핑하는 프로세스입니다. 
래퍼 외부에 정의된 코드의 임의 액세스를 중지하는 보호 래퍼로 간주할 수 있습니다.

In the this program, the variable number1 is made private so that this variable can be accessed and manipulated only by using the methods 
get() and set() that are present within the class. Therefore we can say that, the variable a and the methods set() as well as 
get() have bound together that is encapsulation. There is nothing special about the method names "get()" or "set()" 
- there may be other methods that manipulate the variable number1...all together this is called encapsulation.

이 프로그램에서 number1 변수는 private으로 설정되어 클래스 내에 있는 get() 및 set() 메서드를 통해서만 이 변수에 액세스하고 조작할 수 있습니다. 
따라서 변수와 메서드 set() 및 get()이 함께 묶인 캡슐화라고 말할 수 있습니다. 메소드 이름 "get()" 또는 "set()"에 대해 특별한 것은 없습니다. 
변수 number1을 조작하는 다른 메소드가 있을 수 있습니다...모두 이것을 캡슐화라고 합니다.

데이터에 getter와 setter로 접근하는 거..
*/
#include <iostream> 
using namespace std; 

class EncapsulationExample { 
    private: 
        // we declare a as private to hide it from outside 
        int number1; 
        public: 
        // set() function to set the value of a 
        void setter(int input1) { 
            number1 = input1; 
        } 
        // get() function to return the value of a 
        int getter() { 
            return number1; 
        } 
}; 

// main function 
int main() { 
    EncapsulationExample myInstance; 
    myInstance.setter(10);
    cout << myInstance.getter() << endl; 
    return 0; 
} 
/*
public 접근 제한자: 단어 뜻 그대로 외부 클래스가 자유롭게 사용할 수 있도록 합니다. 
protected 접근 제한자: 같은 패키지 또는 자식 클래스에서 사용할 수 있도록 합니다. 
private 접근 제한자: 단어 뜻 그대로 개인적인 것이라 외부에서 사용될 수 없도록 합니다.
*/
// Inheritance: 상속 (Keyword: Code Reusability를 높인다)
/*
Inheritance is one in which a new class is created that inherits the properties of the already exist class. 
It supports the concept of code reusability and reduces the length of the code in object-oriented programming.
상속은 이미 존재하는 클래스의 속성을 상속하는 새 클래스가 생성되는 것입니다. 
코드 재사용성 개념을 지원하고 객체 지향 프로그래밍에서 코드 길이를 줄입니다.
상속의 종류(어떻게 만드냐에 따라 달라지는 것..):
- 단일 상속 Single Inheritance 하나만 있는거
- 다중 상속 Multiple Inheritance 두개 Super class -> 하나 Subclass Class
- 다단계 상속 Multilevel Inheritance 여러 개층으로 나뉜거
- 계층적 상속 Hierarchical Inheritance 하나 Super Class -> 여러개 Subclass (가장 일반적)
- 하이브리드 상속 Hybrid Inheritance 여러 상속 종류 섞인거
Shape 클래스를 상속 받아서 Rectangle, Triangle, Square 클래스를 만드는 것
*/
#include <iostream>
 
using namespace std;

// Base class
class Shape {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
   protected:
      int width;
      int height;
};

// Derived class
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};
int main(void) {
   Rectangle Rect;
   Rect.setWidth(5);
   Rect.setHeight(7);
   // Print the area of the object.
   cout << "Total area: " << Rect.getArea() << endl;
   return 0;
}

// Polymolphism: 다형성 - Keyword 
/*
 메서드의 이름은 같고 매개변수의 갯수나 타입이 다른 함수를 정의하는 것을 의미한다. ... 
오버로딩(Overloading)
- 메서드의 이름은 같고 매개변수의 갯수나 타입이 다른 함수를 정의하는 것을 의미한다.
- 리턴값만을 다르게 갖는 오버로딩은 작성 할 수 없다.

오버라이딩(Overriding)
- 상위 클래스의 메서드를 하위 클래스가 재정의 하는 것이다.
- 메서드의 이름은 물론 파라메터의 갯수나 타입도 동일해야 하며, 주로 상위 클래스의 동작을 상속받은 하위 클래스에서 변경하기 위해 사용된다.

Polymorphism is that in which we can perform a task in multiple forms or ways. It is applied to the functions or methods.
Polymorphism allows the object to decide which form of the function to implement at compile-time as well as run-time.
Polymorphism allows the object to decide which form of the function to implement at compile-time (overloading) as well as run-time (overriding).

Types of Polymorphism are:
1. Compile-time polymorphism (Method overloading) 
설명:  Compile time polymorphism, also known as Static Polymorphism, refers to the type of Polymorphism that happens at compile time. 
What it means is that the compiler decides what shape or value has to be taken by the entity in the picture.

2. Run-time polymorphism (Method Overriding) - 
설명: Runtime polymorphism, also known as Dynamic Polymorphism, refers to the type of Polymorphism that happens at the run time. 
What it means is it can't be decided by the compiler.

다형성은 여러 형태나 방식으로 작업을 수행할 수 있는 것입니다. 함수나 메소드에 적용됩니다. 
다형성을 사용하면 객체가 런타임뿐만 아니라 컴파일 타임에도 구현할 함수 형식을 결정할 수 있습니다.
다형성의 종류:
1. 컴파일 타임 다형성
2. 런타임 다형성
"""
# Compile-Time Polymorphism 예시.. (함수명 그대로이고, 변수의 갯수와 종류가 변하는 것(Overloading 사용))
// In this program, we will see how multiple functions are created with the same name, 
// but the compiler decides which function to call easily at the compile time itself.
*/
class CompileTimePolymorphism {
   // 1st method with name add
   public: 
   int add(int x, int y){ 
   return x+y;
   }
   // 2nd method with name add
   int add(int x, int y, int z){
   return x+y+z;
   }
   // 3rd method with name add
   int add(double x, int y){ 
   return (int)x+y;
   }
   // 4th method with name add
   int add(int x, double y){ 
   return x+(int)y;
   }
}
class Test{
   static void main(String[] args){
   CompileTimePolymorphism demo=new CompileTimePolymorphism();
   // In the below statement, the Compiler looks at the argument types and decides to call method 1
   System.out.println(demo.add(2,3));
   // Similarly, in the below statement, the compiler calls method 2
   System.out.println(demo.add(2,3,4));
   // Similarly, in the below statement, the compiler calls method 4
   System.out.println(demo.add(2,3.4));
   // Similarly, in the below statement, the compiler calls method 3
   System.out.println(demo.add(2.5,3)); 
   }
}

// Run-time Polymorphism 예시 (함수의 이름은 그대로고.. Bike(SubClass)와 AnyVehicle(Super Class) 클래스의 메소드명이 같고, 
// 서브클래스(Bike)의 메소드가 실행되게 하는 것) - Overriding 오버라이딩 사용
class AnyVehicle {
   public:
    void move(){
   cout << “Any vehicle should move!!” << endl;
   }
}
class Bike extends AnyVehicle {
   public:
    void move(){
   cout << “Bike can move too!!” << endl;
   }
}
class Test {
   public:
   static void main(String[] args) {
   AnyVehicle vehicle = new Bike();
   vehicle.move(); // -> Bike can move too

   // In the above statement, as you can see, the object vehicle is of type AnyVehicle
   // But the output of the below statement will be “Bike can move too!!”, 
   // because the actual implementation of object ‘vehicle’ is decided during runtime vehicle.move();
   vehicle = new AnyVehicle();
   // Now, the output of the below statement will be “Any vehicle should move!!”, 
   vehicle.move(); // -> Any Vehicle should move 
   }
}