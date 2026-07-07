
a=[40,6,8,50,21,7,22,30,11, 90]

b = [i**2 for i in a]

c=[i for i in a if i%2==0] 

d=[i for i in a if i%2==0 and i%5==0]

e=[f"{i}:even" if i%2==0 else f"{i}:odd" for i in a]
print(e)    