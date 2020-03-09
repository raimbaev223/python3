string = str(input('Введите строку: '))

if string.count('f') >= 2:
  print(string.find('f'), string.rfind('f'))
elif string.find('f') == 0:
  print(string.find('f'))
else:
  print(string.find('f'))