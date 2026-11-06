def print_factors(number):
    print('Factors of', number, 'are:')
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
num = int(input('Enter a number:  '))
print_factors(num)