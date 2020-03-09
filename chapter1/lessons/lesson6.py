# while loop работает пока условие истинно. во избежание зацикливания нужна точка выхода
'''i = 0
while i <= 20:
    print('hello +' + str(i))
    i += 1'''

'''password = 'helloworld'
input_ = ''
while input_ != password:
    input_ = input('Enter your password')'''

'''i = 30
while i != 0:
    print(i)
    i -= 1'''

# Генераторы списков

'''diapazon = range(10)
squares = [x ** 2 for x in diapazon]
print(squares)'''
'''
city = 'bishkek'
letters_up = [x.upper() for x in city]
print(letters_up)
print(type(letters_up))
'''
'''range_ = range(1, 101)
even_num = [x for x in range_ if x % 2 == 0]   093217
odd_nums = [x for x in range_ if x % 2 != 0]   189899
print(even_num)
print(odd_nums)'''
'''from datetime import datetime

new_list1 = []
for x in range(1, 1000000):
    new_list1.append(x)


start = datetime.now()
new_list2 = [x for x in range(1, 1000000)]
print(datetime.now() - start)'''
# enumerate создает кортеж из списка [(key1, val1), (key2, val2)]
# генераторы словарей
'''
dict_ = {key: key ** 2 for key in range(1, 10)}
print(dict_)''''''
old_list = ['john', 'raychel', 'peter', 'samanta']
new_dict = {key: value for key, value in enumerate(old_list)}
print(new_dict)'''

#генератор множеств
new_sets = {x for x in range(1, 100)}
print(new_sets)
print(type(new_sets))