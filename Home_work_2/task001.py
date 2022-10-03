# Напишите программу, которая принимает на вход вещественное число и показывает сумму 
# его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input('введите число '))
count = 0
if number < 0:
    number = number * (-1)
for i in str(number):
    if i != '.':
        count += int(i)
print(count)

