from rect import Rect

r1=Rect()  # Create an instance of Rect

r2=Rect(4,2)  # Create another instance of Rect

r1.length=4  # Get length input from user for r1
r1.width=5  # Get width input from user for r1

r1.display()  # Display the dimensions of the rectangle
print(f"Area of Rect{r1.id}: {r1.area()}")  # Display the area of the rectangle
print(f"Perimeter of Rect{r1.id}: {r1.perimeter()}")

r2.display()  # Display the dimensions of the rectangle
print(f"Area of Rect{r2.id}: {r2.area()}")  #

print(f"Total Rect instances created: {Rect.count}")  # Display the total number of Rect instances created 

 # Box , Properties - l,b, h , consturctor, Box count, display, volume, surface area
 # BankAcc - Properties - accNo, accName, balance, constructor, deposit, withdraw, display, getbalance
 # Student - Properties - rollNo, name, hindi, eng, math, sci, sst , total, per, constructor, display, 
 # Note: rollno should be auto generated