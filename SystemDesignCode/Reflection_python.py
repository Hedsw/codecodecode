class MyClass:
    my_var = 1

    def __init__(self):
        pass

    def my_fnc(self, arg):
        print('my_fnc({}) called.'.format(arg))

# 클래스 및 클래스변수 접근
my_class = globals()['MyClass']
print(my_class)
print(my_class.my_var)
#print(my_class.my_fnc(1))

# 객체 생성
my_inst = my_class()
print(my_inst)

# 함수 접근 및 호출
func = getattr(my_inst, 'my_fnc')
print(func)
func(2)
