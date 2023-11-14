#1 class1.py
#2 클래스를 정의

class Person :
    def __init__(self) :
        self.name = " default name"
    def print(self) :
        print('My name is{0}'.format(self.name))

# 2) 인스턴스를 정의
p1 = Person()
p2 = Person()


# 3) 매서드 호출
p1.print()

p1.name = '전우치'

p1.print()
p2.print()

#런타임(코드가 실행중)  -> 인스턴스 보고 없으면 클래스 보고 없으면 전역 봄
Person.title = 'new title'
print(p1.title)
print(p2.title) 
print(Person.title)


