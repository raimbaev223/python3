"""
title = input('Введите заголовок: ')
if title.istitle():
    print('OK мы принимаем твои данные')
else:
    print('Напиши в верхнем регистре')


text = input('Введите текст: ')
if text.islower():
    print(text.upper())
else:
    print(text.lower())

some_text = input('Введите текст: ').lower()
print(some_text.startswith('a'))


some_text = input('Введите текст :').lower()
if some_text.endswith('@gmail.com'):
    print('Это гугл')
elif some_text.endswith('@mail.ru'):
    print('Это мылору')
else:
    print(f'Программа не распознает этот {some_text} email!')

names = ['john', 'raychel', 'peter']
text = ' Hello world '.join(names)
print(text)
# output: john Hello world raychel Hello world peter



print(ord('я'))
# output: 1103


text = 'hello world'
print(text.count('o'))


strip_ = input('введите даннные: ')
print(strip_.strip())
print(strip_.lstrip())
print(strip_.rstrip())

print(len(strip_))
print(len(strip_.strip()))

text = input('text: ')
print(text.swapcase())

OUTPUT:
text: ASDASDASDASD
asdasdasdasd
"""
"""
names = ['Musa', 'Angela', 'John', 'Sanya', 'Jason', 'Veronika', 'Raychal']
for name in names:
    print('Приветствуем тебя {}'.format(name))
    
'{}, {}, {}'.format('b', 'a', 'c')
'{1}, {0}, {2}'.format('b', 'a', 'c')
"""
#Типы данных
#tuple - кортеж
"""
zoo = ('python', 'elephant', 'pinguin', 'wolf', 'tiger', 'lion')
print(type(zoo))
print('number of animals in zoo is', len(zoo))


new_tuple = 'python', 'js', 'c++', 'c#', 'java', 'pascal', 'basic'
print(new_tuple)

empty = tuple(['hello', 'world'])
print(empty)

num = (1)
print(num)
print(type(num))


text = 'Python is the best language!'
text_converted_2_tuple = tuple(text)
print(text_converted_2_tuple)

#out: ('P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 't', 'h', 'e', ' ', 'b', 'e', 's', 't', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', '!')


names = ('Nurbek', 'Erkin', 'Aziz', 'Umida', )
print(names.index('Aziz'))
print(names.count('Aziz'))
"""
# out: 2


