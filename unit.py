total=0
count=0 
while True:
  num = float(input("enter a number: "))

  if num==0:
    break
  total+=num
  count+=1
print("The sum of the numbers is: ",total)
print("The average of the numbers is: ",total/count if count > 0 else 0)