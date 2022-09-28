# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# in 6731 out 17;
# in 0.67 out 13;
# in 198.45 out 27

number = input("Введите число: ")

length = len(str(number))
number = float(number)
number = int(number * 10 ** (length - 2))
sum = 0

for i in range(length +2):
    sum += number % 10
    number = number // 10
print(sum)
