# break statement transfer the control outside the loo
# cause of break in the loom become un natural death of the loop
# break terminate the loop in emergency
# Q. enter a number and check is it prime ot not

num=int(input("Enter a number: "))
i=2
while i<num:  #9
    if num%i==0: 
        break
    i=i+1

if(i==num):
    print(num,"is prime number")
else:
    print(num,"is not prime number")

# print all prime numbers between 1 to 100
