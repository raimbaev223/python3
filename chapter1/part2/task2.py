students = int(input('Количество студентов: '))
apples = int(input('Количество яблок: '))
basket = apples % students
print('Каждый студент получит ' + str(apples // students) + ' яблок. ' + str(basket) + ' яблок останется в корзине.')