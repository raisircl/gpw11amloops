#continue: transfer control at the beginning of the loop
# if continue work then the statement below the continue will not be executed
# Q. print 1-10 and skip 5 and 7
i=0
while i<=10:
    i=i+1
    if(i==5 or i==7):
        continue
    print(i)
