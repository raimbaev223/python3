num1 = int(input('input num1: '))
num2 = int(input('input num2: '))
operator = input('choice operator + - / * ** // %: ')
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '**':
    print(num1 ** num2)
elif operator == '//':
    print(num1 // num2)
elif operator == '%':
    print(num1 % num2)
else:
    print('Калькулятор не распознает введенные данные')