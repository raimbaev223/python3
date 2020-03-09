def polindrome_checking():
    word = str(input('Input word for check: '))
    reversed_word = word[::-1]
    if word == reversed_word:
        print(True)
    else:
        print(False)
polindrome_checking()