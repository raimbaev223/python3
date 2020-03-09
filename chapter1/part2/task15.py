num1 = int(input('your age: '))
num2 = num1 + 1

if num2 % 2 == 1:
    range_ = range(2, num2, 2)
    print(list(range_))
else:
    range_ = range(1, num2, 2)
    print(list(range_))