height=[]
num=int(input("ENter the number of students:"))

for n in range(num):
      numbers=float(input("enter student's height:"))
      height.append(numbers)
print("The Tallest height is:",max(height),"\nThe Shortest height is:",min(height))
