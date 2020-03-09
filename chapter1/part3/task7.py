nums = []
positive = []
negative= []
count_of_nums = int(input('Введите количество чисел для списка: '))
for i in range(0, count_of_nums):
    num = int(input())
    nums.append(num)
print(nums)
def positive_or_negative():
    for num in nums:
        if num < 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)

positive_or_negative()
print(positive)
print(negative)