number = int(input("enter an number: "))
multiplication=1
for digitofnumber in str(number):
  if int(digitofnumber) != 0:
    multiplication*= int(digitofnumber)
print("digits of the number: ",multiplication)