def romanToInt(romanInput):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(romanInput)):
        current = roman[romanInput[i]]
        if i + 1 < len(romanInput):
            next_value = roman[romanInput[i + 1]]
            if current < next_value:
                total = total + current
            else:
                total = total + current
        else:
            total = total + current
    return total
user_input = input('Enter a Roman Numeral: ')
answer = romanToInt(user_input)
print('Integer value:', answer)