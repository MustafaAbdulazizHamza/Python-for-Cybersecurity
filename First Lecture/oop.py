class Vehicle:
    def __init__(self, speed):
        self.__speed = speed
class Car (Vehicle):
    def __init__(self, speed, engine):
        super().__init__(speed)
        self.__engine = engine
vehicle = Vehicle(45)
car = Car(250, 'X')

class Base:
    def __init__(self):
        print('Base.__init__')
class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')
class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')
class C(A,B):
        def __init__(self):
            super().__init__() 
            print('C.__init__')
c = C()