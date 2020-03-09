h1 = int(input('h1: '))
m1 = int(input('m1: '))
s1 = int(input('s1: '))
h2 = int(input('h2: '))
m2 = int(input('m2: '))
s2 = int(input('s2: '))
t1 = m1 * 60 + h1 * 3600 + s1
t2 = m2 * 60 + h2 * 3600 + s2
res = t2 - t1
print(f'The time difference is {res} seconds.')
