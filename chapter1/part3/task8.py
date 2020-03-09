nums1 = []
nums2 = []
count_of_nums = int(input('Введите количество чисел для списка: '))
for i in range(0, count_of_nums):
    num = int(input())
    nums1.append(num)
print(nums1)

def my_func():
    for num in nums1:
        if num < 0:
            num = -1
            nums2.append(num)
        elif num > 0:
            num = 1
            nums2.append(num)

my_func()
print(nums2)


