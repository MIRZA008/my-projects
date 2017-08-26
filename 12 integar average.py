t=0
for c in range(12):
    n=int(input("enter the value:"))
    if n<-273 or n>60:
        c=c-1
        print("invalid value")
    else:
      t=t+n
print("THE AVERAGE WITHOUT INCLUDING THE INVALID NUMBER IS",t/12)
