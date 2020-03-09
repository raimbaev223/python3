def is_even(num):
    if num % 2 == 0:
        print('assert is_even(' + str(num) + ') == True')
    else:
        print('assert is_even(' + str(num) + ') == False')

num = int(input('Please input number:'))
is_even(num)