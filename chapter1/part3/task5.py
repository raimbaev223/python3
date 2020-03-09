string = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
print(str)
Words = string.split()
long = 0
for i in range(1, len(Words)):
    if len(Words[long]) < len(Words[i]):
        long = i

print(Words[long])
