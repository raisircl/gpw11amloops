#private properties (data hinding) - 
#so private members can not access outside the class
class Distance:
    count=0 # class attribute - to keep track of number of instances created
    def __init__(self, feet=0, inch=0):
        self.__feet = feet # private instance attributes
        self.__inch = inch
        Distance.count += 1 # increment the count whenever a new instance is created
        self.id = Distance.count # assign a unique id to each instance based on the count
    
    @property
    def feet(self):
        return self.__feet
    @feet.setter
    def feet(self, value):
        self.__feet = value
    
    @property
    def inch(self):
        return self.__inch
    @inch.setter
    def inch(self, value):
        self.__inch = value
    
    def __str__(self):
        return f"Distance{self.id}: {self.__feet} feet, {self.__inch} inches"
    
    def __add__(self, d2):
        temp = Distance()
        temp.feet = self.feet + d2.feet
        temp.inch = self.inch + d2.inch
        if temp.inch >= 12:
            temp.feet += temp.inch // 12
            temp.inch = temp.inch % 12
        return temp
    @classmethod
    def get_count(cls):
        return cls.count