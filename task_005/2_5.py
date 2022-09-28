# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

# in 10
# out [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     [7, 4, 1, 8, 5, 2, 6, 3, 0, 9] 


import random
size = int(input("Размер списка: "))

numbers = list()
for i in range(size):
    numbers.append(i)
print(numbers)

numbers_new = list()
num = 0
i = 0
while True:
    num = random.randint(0, size -1)
    if num in numbers_new: continue
    else: numbers_new.append(num)
    if len(numbers_new) == size: break
print(numbers_new)
