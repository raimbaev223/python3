'''
==
!=
<
>
<=
>=
and or not
True and True = True
True and False = False
True or False = True
False or True = True
not False = True
not True = False
point = int(input('input your point: '))
if point == 5:
    print('молодец')
elif point == 4:
    print('Ты молодец, осталось немного до отличника')
elif point == 3:
    print('Старайся учиться лучше')
else:
    print('занимайся старательно')'''
'''
is_fb_user = True
is_git_user = True
if is_fb_user and is_git_user:
    print('you can enter the system!')
else:
    print('Sorry, you should have FB and Git accounts')
    '''
'''is_fb_user = True
is_git_user = True
is_user_age_greater_18 = True
user_acc_money = 10100
if (is_fb_user and is_git_user) and (
        is_user_age_greater_18 or user_acc_money > 10000
        ):
    print('you can enter the system!')
else:
    print('Sorry, you should have FB and Git accounts')
'''
'''
users_login = True
user_inst_acc = True
user_gitlab_acc = True
if users_login:
    print('authenticated!')

elif user_gitlab_acc:
    print('has gitlab acc')

elif user_inst_acc:
    print('has inst acc')
'''
'''
nums = list(range(1, 100))
for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print(num, 'foobar')
    elif num % 5 == 0:
        print(num, ' bar')
    elif num % 3 == 0:
        print(num, 'foo')
Ч
exp = 10
js = True
python = True
golang = True
if exp >= 10:
    print('Блок1')
    print('О ты сеньор разраб')
    if python:
        print('Отлично ты знаеш пайтон')
        if golang and js:
            print('Отлично ты гофер и джаваскриптизер')
        print('молодец, ------')
    print('ну ты знаешь много')
    print('продолжение блока 1')
'''
#---------------- for loop / while loop
'''
for _ in range(0, 5):
    print("без циклов не обойтись")
'''
'''pizza = ['1st_tem', '2nd_tem', '3rd_tem', '4th_tem', '5th_tem', '6th_tem', '7th_item', '8th_item']
enumerations = []
for item in pizza:
    new_item = item.split('_')[0]
    enumerations.append(new_item.title())
print(enumerations)'''
'''
str_ = 'hello'
#print(dir(str_))
iterator = str_.__iter__()
#print(type(iterator))
#print(dir(iterator))
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

a = 10
b = 20
a, b = b, a
print(a)
print(b)
'''
