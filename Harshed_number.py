number = int(input())

# Making copy of number for later use
copy = number

# Finding sum of digit
digit_sum = 0

while number:
    digit_sum += number%10
    number //= 10

# Checking divisibility & making decision
if copy%digit_sum == 0:
    print('True')
else:
    print('False')