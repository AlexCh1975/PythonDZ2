# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.

# in 6 out [2, 2, 2, 2, 2, 3] 13

n = int(input("Введите n: "))

numbers = list()
res = 0
sum = 0
for i in range(1, n + 1):
    res = round((1 + 1 / i) ** i)
    print(res, end=', ')
    sum += res
print()
print("sum = {}".format(sum))