def square(num):
  res = num * num
  print('assert square(' + str(num) + ') == ' + str(res))
    
num = int(input('Please input number:'))
square(num)