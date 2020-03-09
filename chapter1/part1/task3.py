def is_odd(num):
    if num % 2 == 1:
        print('assert is_odd(' + str(num) + ') == True')
    else:
        print('assert is_odd(' + str(num) + ') == False')

num = int(input('Please input number:'))
is_odd(num)