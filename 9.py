def is_all_digits_odd(number):
    for digit in str(number):
        if int(digit) % 2 == 0:
            return False
    return True
valid_numbers = []
for number in range(1000, 3001):
    if is_all_digits_odd(number):
        valid_numbers.append(number)
print("@".join(map(str, valid_numbers)))