class A:
    def __init__(self , name ):
        self.name = name


class B(A):
    def __init__(self ,age ):
        self.age = age

class C:
    def r(self):
        print(f'cтолько лет методу {self.age}')

class V:
    def f(self):
        print(f"имя метода {self.name}")

class J(V, C, B, A):
    def __init__(self , name , age):
        A.__init__(self, name )
        B.__init__(self,age)


j = J('Alim', 15)
j.f()
j.r()