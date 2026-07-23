class quadriletral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

class rectangle(quadriletral):
    def __init__(self, a=1, b=1):
        super().__init__(a, b, a, b)
    
    def __add__(self,r2):
        temp=rectangle()
        temp.a=self.a+r2.a
        temp.b=self.b+r2.b
        return temp
    def __str__(self):
        return f"Dimension is {self.a} x {self.b}"
    
    def area(self):
        return self.a * self.b    

class square(rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    def area(self):
        x=pow(self.a,2)
        print("Area of square is:",x)    

s1=square(5)
s1.area()
print(f"Perimeter of square is: {s1.perimeter()}")


r1=rectangle(5,6)
r2=rectangle(7,8)
r3=r1+r2
print(f"Area of rectangle is: {r3.area()}")
print(f"Perimeter of rectangle is: {r3.perimeter()}")
