# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2) == (2 * (2 + 2)))

# 4th program
number_str = '123.456'
number = float(number_str)
number *= 10
first_digit_after_decimal = int(number) % 10
print(first_digit_after_decimal)  