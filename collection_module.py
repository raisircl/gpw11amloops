import collections
student=collections.namedtuple('Student', ['name', 'age', 'grade'])
s1=student('John', 20, 'A')

print(s1)

print(s1.name)
print(s1.age)
print(s1.grade)
