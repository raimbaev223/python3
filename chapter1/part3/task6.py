evens = []
odds = []
nums = []
count_of_nums = int(input('Введите количество чисел для списка: '))
for i in range(0, count_of_nums):
    num = int(input('Введите число: '))
    nums.append(num)
print(nums)
for num in nums:
    if num % 2 == 0:
        evens.append(num)
    elif num % 2 != 0:
        odds.append(num)
print(evens)
print(len(evens))
print(odds)
print(len(odds))