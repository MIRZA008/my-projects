num=int(input("enter the values:"))
num1=int(input("enter the number of values:"))
sum=0
while(num!=0):
    remainder=num%10
    sum=sum+remainder
    num=num//10
print("the average of the values you have entered is:",sum/num1)

    
    
