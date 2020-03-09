# Lists
'''
new_list = []
empty_list = list()
some_details = ['a', 'b', [1, 2], 'd', (1, 2)]
print(type(new_list))
print(empty_list)
print(some_details)

list()
names = ('john', 'raychel')
print(list(names))

range_ = range(30, 1, -2)
print(type(range_))
print(range_)
new_list = list(range_)
print(new_list)
print(type(new_list))

some_list = [1, 2, 3, 4, 5,]
some_list.append(6)
some_list.append('numbers')
print(some_list)

list1 = ['user1', 'user2', 'user3']
list2 = ['John', 'Raychel', 'Angela', 'Peter']
list1.extend(list2)
print(list1)
print(list2)
list1.insert(0, 'user0')
print(list1)

insert method
remove method
index method



laptops = ['lenovo', 'samsung', 'asus', 'acer']
print('before', laptops)
laptops.remove('asus')
print('after', laptops)


lang = ['python', 'go', 'php', 'js', 'java', 'c++', 'c#']
print('before', lang.pop())
lang.pop()
lang.pop(1)
print('after', lang)


movies = ['1+1', '2+1', 'avatar']
print(movies.index('1+1'))

'''
students = ['Mahmud', 'Ahmed', 'Khabib', 'Connor', 'Mike', 'Ahmed']
print((students.count('Ahmed')))

list123123 = [1, 2, 3, 4, 5, 6, 7]
list123123.reverse()
print(list123123)
'''
########################SORT

arrays = [1, 5, 6, 434, 12, 123, 3245, 3, 23346346, 2312]
print(arrays)
arrays.sort()
print(arrays)
arrays.sort(reverse=True)
print(arrays)

name = ['John', 'Raychel', 'Deineries', 'Ahmed,', 'Mahmud']
name.sort(key=len)
print(name)

def take2nd(elem):
    return elem[1]
random = [(2, 2), (3, 4), (5, 5)]
random.sort(key=take2nd)
print('Sorted list: ', random=True)
'''
##########################---------------COPY---------------
'''
cars = ['subaru', 'mersedes', 'bmw', 'honda', 'toyota', 'taz', 'zil', 'gaz']
print(cars)
new_cars = cars.copy()
new_cars[3] = 'Lisaped'
print(new_cars)
print(cars)
'''
'''######################-------------DEEPCOPY
import copy
list_ = [1, 2, 3, [4, 5, 6]]
print('original - ', list_)
list_2 = copy.deepcopy(list_)
print('Copy', list_2)
list_2[3][0] = 'changed'
print('copyed - ', list_2)
print(list_)'''


# ----------------------------CLEAR-----------------------

'''list_ = [1, 2, 4, 5, 2, 5, 5, 6]
print(list_)
list_.clear()
print(list_)
del list_[0]
print(list_)'''

# ---------dict/словари--------
'''
dict_ = {}
dict1 = {'key': 'val', 'key2': 'val2', 'key3': 'val3'}
print(dict1)
func_dict = dict(instrument='guitar', car='subaru')
print(type(dict_))
print(dict1)
print(func_dict)
tuple_dict = dict([('ru', 'russia'), ('us', 'usa'), ('kg', 'kyrgizstan')])
print(tuple_dict)
'''
'''
some_dict = {0: 1, 1: 2, 1.5: 2.5, True: False, False: True, (1, 2, 3): [1, 2, 3], 0: 123124124123}
print(some_dict)'''