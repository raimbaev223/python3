num = int(input('input number: '))
factorial = 1
if num < 0:
    print('***** SUB ***** ZERO *****')
if num == 0:
    print("it\'s zero")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(f'factorial of {num} = {factorial}')

