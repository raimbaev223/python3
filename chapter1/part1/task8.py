def test_choice_to_number():
    if name == 'Usain':
        print(1)
    elif name == 'Erkin':
        print(2)
    elif name == 'Azamat':
        print(3)
        
def test_number_to_choice():
    if name == '1':
        print('Usein')
    elif name == '2':
        print('Erkin')
    elif name == '3':
        print('Azamat')

name = str(input('Enter choice or number: '))
test_number_to_choice()
test_choice_to_number()