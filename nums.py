import random 

guess = int(input('Напишите количество чисел: '))
nums = [random.randint(1, guess) for i in range(1, guess + 1)]

def find_missing_nums(nums):
    normal_array = [i for i in range(1, guess + 1)]
    arr = []
    for i in range(len(normal_array)):
        if normal_array[i] not in nums:
            arr.append(normal_array[i])
    print(arr)

find_missing_nums(nums)