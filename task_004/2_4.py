# Напишите программу, которая принимает на вход 2 числа. Задайте список
# из N элементов, заполненных числами из промежутка [-N,N]. Найдите произведение
# элементов на указанных позициях (не индексах).

# in position one: 3
#    position two: 4
#    number of elements: 5
# out [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] 6

position_one = int(input("Введите первую позицию: "))
position_two = int(input("Введите вторую позицию: "))
n = int(input("Число элементов списка: ")) 

numbers = list()

i = n * -1

while i <= n:
    numbers.append(i)
    i += 1    
print(numbers)
if len(numbers) < position_one or len(numbers) < position_two:
    print("Заданные позиции находятся в не диапазона списка!")
else: print(numbers[position_one - 1] * numbers[position_two - 1])