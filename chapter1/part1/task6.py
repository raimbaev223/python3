#def bigger_guy():
#    num1 = input('Please input num1: ')
#    num2 = input('Please input num2: ')
#    nums = [num1, num2]
#    nums.sort()
#    print('assert bigger_guy(' + num1 + ', ' + num2 + ') == ' + nums[-1])
#    print(nums)
#
#bigger_guy()

def bigger_guy():
    num1 = input('Please input num1: ')
    num2 = input('Please input num2: ')
    if num1 > num2:
        print('assert bigger_guy(' + num1 + ', ' + num2 + ') == ' + num1)
    elif num2 > num1:
        print('assert bigger_guy(' + num1 + ', ' + num2 + ') == ' + num2)
    elif num2 == num1:
        print('You stupid!!! ' + num1 + ' == ' + num2)

bigger_guy()