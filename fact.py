num=int(input("Enter a number: "))
f=1
for i in range(1,num+1):
    print(f"{i}x",end="")
    f=f*i
print(f"\b={f}")

#1x2x3x4x5=120\b