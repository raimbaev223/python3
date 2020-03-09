group_1 = int(input("Students in class 1: "))
group_2 = int(input("Students in class 2: "))
group_3 = int(input("Students in class 3: "))

if (group_1 % 2) == 0:
  descs_1 = int(group_1 / 2)
elif (group_1 % 2) == 1:
  descs_1= int(group_1 / 2) + 1

if (group_2 % 2) == 0:
  descs_2= int(group_2 / 2)
elif (group_2 % 2) == 1:
  descs_2 = int(group_2 / 2) + 1

if (group_3 % 2) == 0:
  descs_3 = int(group_3 / 2)
elif (group_3 % 2) == 1:
  descs_3 = int(group_3 / 2) +1
res = descs_1 + descs_2 + descs_3
print(f'Total descs needed is: {res}')