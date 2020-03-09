# continue the topic dict

# fromkeys
'''dict_ = dict.fromkeys(['key1', 'key2'])
print(dict_)
print(type(dict_))
test_var = dict.fromkeys(['name', 'name2'], 'testUser')
print(test_var)'''

'''dict_ = {'name': 'John', 'lastname': 'Snow'}
print(dict_['name'], dict_['lastname']) 
# John Snow'''

'''osme_data = {1: 5, 2: 8, 3: 4}
osme_data[4] = 10 +5
print(osme_data)
osme_data[10] = 20
print(osme_data)
# {1: 5, 2: 8, 3: 4, 4: 15}
# {1: 5, 2: 8, 3: 4, 4: 15, 10: 20}'''
# get
'''
cars = {'mercedes': 'mclaren', 'bmw': 'samuray', 'toyota': 'camry'}
print(cars.get('toyota'))
# camry
# отличается от вывода через [] тем что не дает ошибки при отсутствии ключа
'''
# keys
'''
univer = {'kgtu': 'Politex', 'auca': 'American', 'krsu': 'slavyan'}
print(univer.keys())
keys = list(univer.keys())
print(keys)'''
# values
'''
courses = {'sherlok': 'english', 'makers': 'python'}
print(courses.values())
val = list(courses.values())
print(val)
# dict_values(['english', 'python'])
# ['english', 'python']
'''
# items() создает список с кортежами из двух значений
'''
example_dict = {'key': 'val', 'key1': 'val1', 'key2': 'val2'}
pairs = example_dict.items()
print(pairs)
pairs = list(example_dict.items())
print(pairs)'''
# pop
'''
dict_ = {'kgtu': 'Politex', 'auca': 'American', 'krsu': 'slavyan'}
print(dict_)
krsu = dict_.pop('krsu')
print(dict_)
print(krsu)'''
# popitem
'''
dict_ = {'student': 'john', 'student2': 'raychel'}
deleted =dict_.popitem()
print(dict_)
'''
# update
'''laptops = {'acer': '1215', 'macbook': 'pro', 'asus': 'dzenbook'}
computers = {'lenovo': 'yoga', 'acer': '1913'}
print(laptops)
laptops.update(computers)
print(laptops)'''
# setdefault
'''
dict_ = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
new = dict_.setdefault('key2')
print(new)
dict_.setdefault('key4', 'val4')
print(dict_)
# val2
# {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
'''
# -------------------------------------------sets---------------------------
'''
newSet = set()
print(type(newSet))
print(newSet)

unique_numbers = {1, 2, 3, 4, 5, 6}
print(unique_numbers)
print(type(unique_numbers))
'''
# add
'''
sets = {1, 2}
sets.add(3)
print(sets)
'''
# remove
'''
sets = {1, 2, 3, 4}
print(sets)
#sets.remove(1)
print(sets)
'''
# discard
'''
sets.discard(2)
print(sets)
'''
# pop
'''
set_ = {1, 2, 3, 4, 5, 6, 7, 9, 11, 212}
print(set_)
a = set_.pop()
print(set_)
print(a)
'''
