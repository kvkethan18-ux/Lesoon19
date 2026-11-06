# Armstrong number .........
number = int(input('Enter a number'))
original = number
digits = len(str(number))
total = 0
temp = number
while temp > 0:
    digit = temp % 0
    total = total + digit ** digits
    temp = temp // 10
if total == original:
    print('The number is an armstrong number')
else:
    print('The number is  not an armstrong number.')