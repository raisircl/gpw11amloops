def get_result(h,e,m,sci,sst):
    total=h+e+m+sci+sst
    per=total/5
    return total,per

t,p=get_result(90,80,70,85,75)
print("Total marks:",t)
print("Percentage:",p)
