num1 = input('Enter number of inputs: ')
num = []
sum = 0
for i in range(int(num1)):
    n = input(f'Enter number {i+1}: ')
    num.append(int(n))
    sum += int(n)

average = sum / int(num1) if int(num1) > 0 else 0

print('average:{0} '.format(average))