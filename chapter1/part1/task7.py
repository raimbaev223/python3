def biggest_guy():
    num1 = int(input('Please input num1: '))
    num2 = int(input('Please input num2: '))
    num3 = int(input('Please input num3: '))
    if num1 >= num2 and num1 >= num3:
        print('assert biggest_guy(' + str(num1) + ', ' + str(num2) + ', ' + str(num3) + ') == ' + str(num1))
    elif num2 >= num1 and num2 >= num3:
        print('assert biggest_guy(' + str(num1) + ', ' + str(num2) + ', ' + str(num3) + ') == ' + str(num2))
    elif num3 >= num1 and num3 >= num1:
        print('assert biggest_guy(' + str(num1) + ', ' + str(num2) + ', ' + str(num3) + ') == ' + str(num3))

biggest_guy()