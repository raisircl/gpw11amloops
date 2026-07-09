from distance import Distance

d1 = Distance()
d1.feet = 5 # setter - 5 will passed to value variable of setter method
d1.inch = 8

d2=Distance(3,4)

d3=Distance()

d3 = d1 + d2 

#print(f"Distance: {d1.feet} feet, {d1.inch} inches") # getter - will return the value of private instance attributes

print(d1)
print(d2)
print(d3)

print(f"Total Distance instances created: {Distance.get_count()}")  # Display the total number of Distance instances created