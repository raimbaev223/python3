num = []
flag = 'yes'
while flag[0] == "y":
  add = int(input('enter a num to add in list:\n'))
  num.append(add)
  flag = input('if you want add a number, input yes:')
print(num)
for n in num:
  if n % 2 == 0:
    print(n)
